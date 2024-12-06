import copy


class Field:
    BLANK = 0
    VISITED = 1
    OBSTACLE = 2


class Direction:
    def __init__(self):
        self.dirs = (
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0),
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
        self.looped = False
        self.remembered_turns = []

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

    def is_remembered_turn(self):
        for x, y, dx, dy in self.remembered_turns:
            if (
                x == self.x
                and y == self.y
                and dx == self.direction.x
                and dy == self.direction.y
            ):
                return True

        return False

    def move(self):
        x = self.x + self.direction.x
        y = self.y + self.direction.y

        if self.is_outside(x=x, y=y):
            return False

        new_pos = self.map[y][x]

        if new_pos == Field.OBSTACLE:
            if self.is_remembered_turn():
                self.looped = True

                return False

            self.remembered_turns.append(
                (self.x, self.y, self.direction.x, self.direction.y)
            )
            self.direction.turn_right()
            self.move()

            return True

        self.x = x
        self.y = y

        if new_pos == Field.BLANK:
            self.map[y][x] = Field.VISITED

        return True


class Task:
    def __init__(self, input):
        self.guard = self.get_guard(input)

        self.guard_x = self.guard.x
        self.guard_y = self.guard.y

        self.map = copy.deepcopy(self.guard.map)
        while self.guard.move():
            pass

        self.sum = 0
        positions = self.get_visited_positions()
        for pos in positions:
            map = copy.deepcopy(self.map)
            x, y = pos
            map[y][x] = Field.OBSTACLE

            guard = Guard(self.guard_x, self.guard_y)
            guard.set_map(map)

            while guard.move():
                pass

            if guard.looped:
                self.sum += 1

    def get_visited_positions(self):
        pos = []
        for y, row in enumerate(self.guard.map):
            for x, field in enumerate(row):
                if field == Field.VISITED:
                    pos.append((x, y))

        for i, (x, y) in enumerate(pos):
            if x == self.guard_x and y == self.guard_y:
                del pos[i]

        return pos

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
