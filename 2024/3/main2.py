import re


def get_muls(stream):
    commands = re.findall(r"(mul\(\d+,\d+\))|(don't\(\))|(do\(\))", stream)
    add = True
    muls = []
    for command in commands:
        if add and command[0]:
            muls.append(command[0])
        elif command[1]:
            add = False
        elif command[2]:
            add = True

    return muls


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        stream = "".join(file.readlines())

    muls = get_muls(stream)
    sum = 0
    for mul in muls:
        v1, v2 = re.findall(r"\d+", mul)
        sum += int(v1) * int(v2)

    print(sum)
