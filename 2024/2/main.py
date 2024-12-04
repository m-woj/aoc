if __name__ == "__main__":
    file = open("input.txt", "r")
    reports = []
    for line in file:
        levels = [int(i) for i in line.split()]
        reports.append(levels)

    safe = 0
    for report in reports:
        diff = report[0] - report[1]
        d = abs(diff)
        if d < 1:
            continue
        if d > 3:
            continue

        length = len(report) - 1
        for i in range(1, length):
            diff2 = report[i] - report[i + 1]

            if diff2 * diff < 0:
                break

            diff = diff2

            d = abs(diff2)
            if d < 1:
                break
            if d > 3:
                break

            if i == length - 1:
                safe += 1

    print(safe)
