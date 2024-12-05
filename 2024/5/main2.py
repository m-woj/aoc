class Rule:
    before: frozenset[int]
    after: frozenset[int]

    def __init__(self, before, after):
        self.before = frozenset(before)
        self.after = frozenset(after)

    def __repr__(self):
        return str(self.before) + " | " + str(self.after)


class Task:
    def __init__(self, input):
        self.rules, self.manuals = self.get_rules_and_manuals(input)
        self.manuals = self.get_invalid_manuals()
        self.manuals = self.correct_manuals()
        self.sum = self.get_sum()

    @staticmethod
    def get_rules_and_manuals(input):
        raw_rules = []
        manuals = []

        file = open(input, "r")
        while line := file.readline():
            if line != "\n":
                raw_rules.append(line.strip())
            else:
                break

        while line := file.readline():
            manuals.append(line.strip())

        file.close()

        manuals = [manual.split(",") for manual in manuals]
        for manual in manuals:
            for i in range(len(manual)):
                manual[i] = int(manual[i])

        numbers = set()
        for i in range(len(raw_rules)):
            b, a = raw_rules[i].split("|")
            raw_rules[i] = (int(b), int(a))
            numbers.update(raw_rules[i])

        rules = {}
        for n in numbers:
            before = []
            after = []
            for b, a in raw_rules:
                if n == b:
                    after.append(a)
                elif n == a:
                    before.append(b)

            rule = Rule(before=before, after=after)
            rules[n] = rule

        return rules, manuals

    def get_invalid_manuals(self):
        valid_manuals = []
        for manual in self.manuals:
            if not self.is_valid_manual(manual):
                valid_manuals.append(manual)

        return valid_manuals

    def is_valid_manual(self, manual):
        for pos in range(len(manual)):
            if not self.is_valid_pos(pos, manual):
                return False

        return True

    def is_valid_pos(self, pos: int, manual):
        n = manual[pos]
        rule = self.rules.get(n)
        if not rule:
            return True

        befores = manual[:pos]
        for b in befores:
            if b in rule.after:
                return False

        afters = manual[pos + 1 :]
        for a in afters:
            if a in rule.before:
                return False

        return True

    def correct_manuals(self):
        for i in range(len(self.manuals)):
            self.manuals[i] = self.correct_manual(self.manuals[i])

        return self.manuals

    def correct_manual(self, manual):
        for pos in range(len(manual)):
            if not self.is_valid_pos(pos, manual):
                manual = self.correct_pos(pos, manual)

        return manual

    def correct_pos(self, pos, manual):
        n = manual[pos]
        rule = self.rules[n]

        befores = manual[:pos]
        afters = manual[pos + 1 :]
        nbefores = []
        nafters = []

        i = 0
        while i < len(befores):
            b = befores[i]
            if b not in rule.before:
                del befores[i]
                nafters.append(b)

            i += 1

        i = 0
        while i < len(afters):
            a = afters[i]
            if a not in rule.after:
                del afters[i]
                nbefores.append(a)

            i += 1

        befores = self.correct_manual(befores + nbefores)
        afters = self.correct_manual(afters + nafters)

        return befores + [n] + afters

    def get_sum(self):
        sum = 0
        for manual in self.manuals:
            val = manual[len(manual) // 2]
            sum += val

        return sum


if __name__ == "__main__":
    print(Task("input.txt").sum)
