class Task:
    def __init__(self, input):
        self.t = []
        with open(input, "r") as file:
            for line in file.readlines():
                self.t.append(line.strip())

        self.maxh = len(self.t) - 1
        self.maxw = len(self.t[0]) - 1

        xs_pos = self.get_xs_pos()

        self.dirs = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.dirs.append((i, j))

        self.dirs.pop(4)

        self.sum = 0
        for pos in xs_pos:
            self.sum += self.xmas_num(pos)

    def get_xs_pos(self):
        pos = []
        for h in range(self.maxh + 1):
            row = self.t[h]
            for w in range(self.maxw + 1):
                if row[w] == "X":
                    pos.append((h, w))

        return pos

    def s(self, h, w):
        return self.t[h][w]

    def is_xmas(self, pos, dir):
        word = "X"
        h, w = pos
        dh, dw = dir
        for i in range(1, 4):
            h_ = h + dh * i
            if h_ < 0:
                return False

            if h_ > self.maxh:
                return False

            w_ = w + dw * i
            if w_ < 0:
                return False

            if w_ > self.maxw:
                return False

            word += self.s(h_, w_)

        if word == "XMAS":
            return True

        return False

    def xmas_num(self, pos):
        num = 0
        for dir in self.dirs:
            if self.is_xmas(pos, dir):
                num += 1

        return num


if __name__ == "__main__":
    task = Task("input.txt")
    print(task.sum)
