if __name__ == "__main__":
    file = open("input.txt", "r")
    first = []
    second = []
    for line in file:
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))

    first.sort()
    second.sort()

    sum = 0
    for f in first:
        pos = -1
        for p, s in enumerate(second):
            if s == f:
                pos = p
                break
            elif s > f:
                break

        if pos < 0:
            continue

        occurences = 1
        second = second[pos + 1 :]
        for j in second:
            if j == f:
                occurences += 1
            else:
                break

        sum += f * occurences

    print(sum)
