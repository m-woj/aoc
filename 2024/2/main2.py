def diff_ok(d):
    if d < 1:
        return False
    if d > 3:
        return False

    return True


def retake(report, index):
    for i in range(max(index - 1, 0), index + 2):
        r = report[:]
        del r[i]
        if report_ok(r, True):
            return True

    return False


def report_ok(report, nested=False):
    diff = report[0] - report[1]
    d = abs(diff)
    if not diff_ok(d):
        if nested:
            return False
        else:
            return retake(report, 0)

    length = len(report) - 1
    for i in range(1, length):
        diff2 = report[i] - report[i + 1]

        if diff2 * diff < 0:
            if nested:
                return False
            else:
                return retake(report, i)

        diff = diff2

        d = abs(diff2)
        if not diff_ok(d):
            if nested:
                return False
            else:
                return retake(report, i)

    return True


if __name__ == "__main__":
    file = open("input.txt", "r")
    reports = []
    for line in file:
        levels = [int(i) for i in line.split()]
        reports.append(levels)

    safe = 0
    for i, report in enumerate(reports):
        if report_ok(report, False):
            safe += 1

    print(safe)
