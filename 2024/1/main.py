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
    for i in range(len(first)):
        sum = sum + abs(first[i] - second[i])

    print(sum)
