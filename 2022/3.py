import util


def off_letter(rucksack: str):
    left = rucksack[:len(rucksack) // 2]
    right = rucksack[len(rucksack) // 2:]
    return find_common(left, right)


def find_common(*strings):
    s = set(strings[0])
    for st in strings:
        s.intersection_update(set(st))
    return list(s)[0]


def letter_priority(letter: str) -> int:
    prio = ord(letter) - 96
    if letter.isupper():
        prio += 58  # 32 + 26
    return prio


data = util.load_input(3)
print("p1:", sum(letter_priority(off_letter(line)) for line in data))
print("p2:", sum(letter_priority(find_common(*data[i:i+3])) for i in range(0, len(data), 3)))
