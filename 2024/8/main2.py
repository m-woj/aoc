from collections import defaultdict


class Task:
    def __init__(self, input: str):
        self.max_x, self.max_y = None, None
        self.antenas = self.get_antenas(input)
        self.antinodes = self.get_antinodes()
        self.sum = 0
        for positions in self.antinodes.values():
            self.sum += len(positions)

    def get_antenas(self, input):
        antenas = defaultdict(list)
        file = open(input, "r")
        lines = file.readlines()
        self.max_y = len(lines) - 1
        self.max_x = len(lines[0]) - 2
        for y, line in enumerate(lines):
            for x, sign in enumerate(line.strip()):
                if sign == ".":
                    continue

                antenas[sign].append((x, y))

        return dict(antenas)

    def get_antinodes(self):
        antinodes = defaultdict(set)
        for positions in self.antenas.values():
            for f in range(len(positions) - 1):
                fx, fy = positions[f]
                for sx, sy in positions[f + 1 :]:
                    antinodes[fx].add(fy)
                    antinodes[sx].add(sy)

                    dx = fx - sx
                    dy = fy - sy

                    x = fx + dx
                    y = fy + dy
                    while self.is_on_map(x, y):
                        antinodes[x].add(y)
                        x += dx
                        y += dy

                    x = sx - dx
                    y = sy - dy
                    while self.is_on_map(x, y):
                        antinodes[x].add(y)
                        x -= dx
                        y -= dy

        return antinodes

    def is_on_map(self, x, y):
        if x < 0:
            return False

        if x > self.max_x:
            return False

        if y < 0:
            return False

        if y > self.max_y:
            return False

        return True

    def print_map(self, input):
        file = open(input, "r")
        lines = file.readlines()
        for y, line in enumerate(lines):
            pline = str()
            for x, sign in enumerate(line.strip()):
                if x in self.antinodes and y in self.antinodes[x]:
                    if sign == ".":
                        pline += "#"
                    else:
                        pline += "@"
                else:
                    pline += sign

            print(pline)


if __name__ == "__main__":
    print(Task("input.txt").sum)
