import re
from itertools import zip_longest

import util

unnamed_stacks = []
named_stacks = {}
instructions = []
for line in util.load_input(5):
    if not line.strip():
        continue
    if not line.startswith("move"):
        # stacks
        if "[" not in line:
            named_stacks = {name: data for name, data in zip(line.split(), unnamed_stacks)}
            continue
        for letter, list_ in zip_longest(line[1::4], unnamed_stacks):
            if list_ is None:
                list_ = []
                unnamed_stacks.append(list_)
            if letter != " ":
                list_.insert(0, letter)
    else:
        # move instructions
        count, src, dst = m = re.findall(r"\d+", line)
        # this could be a pretty slice operation but whatever
        moved_list = []
        for _ in range(int(count)):
            element = named_stacks[src].pop()
            # part 1
            # moved_list.append(element)
            # part 2
            moved_list.insert(0, element)
        named_stacks[dst].extend(moved_list)

print("".join(stack[-1] for stack in named_stacks.values()))
