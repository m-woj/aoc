class Field:
    BLANK = 0
    VISITED = 1
    OBSTACLE = 2


class Direction:
    def __init__(self):
        self.dirs = (
            (0, -1),  # up
            # (1, -1),
            (1, 0),
            # (1, 1),
            (0, 1),
            # (-1, 1),
            (-1, 0),
            # (-1, -1),
        )

        self.pos = 0

    def turn_right(self):
        self.pos += 1
        if self.pos > 3:
            self.pos = 0

    @property
    def x(self):
        return self.dirs[self.pos][0]

    @property
    def y(self):
        return self.dirs[self.pos][1]


class Guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Direction()  # up
        self.visited_num = 1

    def set_map(self, map):
        self.max_x = len(map[0]) - 1
        self.max_y = len(map) - 1
        self.map = map

    def is_outside(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y

        if x > self.max_x:
            return True

        if x < 0:
            return True

        if y > self.max_y:
            return True

        if y < 0:
            return True

        return False

    def move(self):
        x = self.x + self.direction.x
        y = self.y + self.direction.y

        if self.is_outside(x=x, y=y):
            return False

        new_pos = self.map[y][x]

        if new_pos == Field.OBSTACLE:
            self.direction.turn_right()
            self.move()

            return True

        self.x = x
        self.y = y

        if new_pos == Field.BLANK:
            self.map[y][x] = Field.VISITED
            self.visited_num += 1

        return True


class Task:
    def __init__(self, input):
        guard = self.get_guard(input)
        while guard.move():
            pass

        self.sum = guard.visited_num

    def get_guard(self, input):
        map = []
        guard = None
        file = open(input, "r")
        for y, line in enumerate(file.readlines()):
            row = []
            for x, sign in enumerate(line.strip()):
                if sign == ".":
                    row.append(Field.BLANK)
                elif sign == "#":
                    row.append(Field.OBSTACLE)
                else:
                    row.append(Field.VISITED)
                    guard = Guard(x, y)

            map.append(row)

        guard.set_map(map)

        return guard


if __name__ == "__main__":
    print(Task("input.txt").sum)
