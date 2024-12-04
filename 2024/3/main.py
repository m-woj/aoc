import re


def get_muls(stream):
    return re.findall(r"mul\(\d+,\d+\)", stream)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        stream = "".join(file.readlines())

    muls = get_muls(stream)
    sum = 0
    for mul in muls:
        v1, v2 = re.findall(r"\d+", mul)
        sum += int(v1) * int(v2)

    print(sum)
