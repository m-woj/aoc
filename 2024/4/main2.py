class Task:
    def __init__(self, input):
        self.t = []
        with open(input, "r") as file:
            for line in file.readlines():
                self.t.append(line.strip())

        self.maxh = len(self.t) - 1
        self.maxw = len(self.t[0]) - 1

        as_pos = self.get_as_pos()

        self.dirs = ((1, 1), (1, -1))

        self.sum = 0
        for pos in as_pos:
            if self.is_xmas(pos):
                self.sum += 1

    def get_as_pos(self):
        pos = []
        for h in range(self.maxh + 1):
            row = self.t[h]
            for w in range(self.maxw + 1):
                if row[w] == "A":
                    pos.append((h, w))

        return pos

    def s(self, h, w):
        return self.t[h][w]

    def hlim(self, h):
        if h < 0:
            return False

        if h > self.maxh:
            return False

        return True

    def wlim(self, w):
        if w < 0:
            return False

        if w > self.maxw:
            return False

        return True

    def is_mas(self, pos, dir):
        h, w = pos
        dh, dw = dir

        hh = h + dh
        hho = h - dh
        if not (self.hlim(hh) and self.hlim(hho)):
            return False

        ww = w + dw
        wwo = w - dw
        if not (self.wlim(ww) and self.wlim(wwo)):
            return False

        s = self.s(hh, ww) + self.s(hho, wwo)
        if "M" not in s:
            return False

        if "S" not in s:
            return False

        return True

    def is_xmas(self, pos):
        for dir in self.dirs:
            if not self.is_mas(pos, dir):
                return False

        return True


if __name__ == "__main__":
    task = Task("input.txt")
    print(task.sum)
