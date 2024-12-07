class Equation:
    output: int
    vars: list[int]

    def __init__(self, output, vars):
        self.output = output
        self.vars = tuple(vars)

    def is_resolveable(self, left_val=0, vars=[]):
        if not vars:
            vars = self.vars

        if not left_val:
            left_val = vars[0]
            vars = vars[1:]

        if left_val == self.output and not vars:
            return True

        if not vars:
            return False

        if left_val > self.output:
            return False

        var = vars[0]
        added = left_val + var
        multiplied = left_val * var

        combined = int(str(left_val) + str(var))

        if len(vars) == 1:
            return (
                added == self.output
                or multiplied == self.output
                or combined == self.output
            )

        vars = vars[1:]
        return (
            self.is_resolveable(added, vars)
            or self.is_resolveable(multiplied, vars)
            or self.is_resolveable(combined, vars)
        )

    def __repr__(self):
        return f"{self.output} = {self.vars}"


class Task:
    def __init__(self, input):
        self.sum = 0
        equations = self.get_equations(input)
        for equation in equations:
            if equation.is_resolveable():
                self.sum += equation.output

    def get_equations(self, input):
        equations = []
        file = open(input, "r")
        for line in file.readlines():
            output, vars = line.split(":")
            vars = vars.strip()
            vars = [int(v) for v in vars.split(" ")]
            equations.append(Equation(int(output), vars))

        return equations


if __name__ == "__main__":
    print(Task("input.txt").sum)
