import util


def range_contains(elf1, elf2):
    return elf1[0] <= elf2[0] and elf1[1] >= elf2[1]


def range_overlaps(elf1, elf2):
    return len(set(range(elf1[0], elf1[1] + 1)).intersection(set(range(elf2[0], elf2[1] + 1)))) != 0


parsed = [[[int(x) for x in elf.split("-")] for elf in line.split(",")] for line in util.load_input(4)]
print(
    "p1:", sum(
        1 for elf1, elf2 in parsed
        if range_contains(elf1, elf2) or range_contains(elf2, elf1)
    )
)
print(
    "p2:", sum(
        1 for elves in parsed
        if range_overlaps(*elves)
    )
)
