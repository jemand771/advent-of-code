import re
from collections.abc import Callable
from dataclasses import dataclass

import util


@dataclass
class Monkey:
    index: int
    items: list[int]
    operation: Callable[[int], int]
    modulo: int
    throw_to_map: dict[bool, int]
    inspect_counter = 0


class State:
    def __init__(self):
        self.monkeys = {}

    def run_round(self, divide_worry_by):
        for monkey in self.monkeys.values():
            while monkey.items:
                monkey.inspect_counter += 1
                worry = monkey.operation(
                    monkey.items.pop(0)
                ) // divide_worry_by
                if worry == 2080:
                    print()
                is_divisible = not worry % monkey.modulo
                to = self.monkeys[monkey.throw_to_map[is_divisible]]
                to.items.append(worry)


def main():
    print("p1:", get_score(rounds=20, divide_worry_by=3))
    print("p2:", get_score(rounds=10000, divide_worry_by=1))


def get_score(rounds, divide_worry_by):
    state = State()
    read_input(state)
    for i in range(rounds):
        print(f"running round {i}/{rounds} ({(i+1) / rounds:.0%})")
        state.run_round(divide_worry_by)
    for monkey in state.monkeys.values():
        print("monkey", monkey.index, "-", " ".join(str(x) for x in monkey.items))
    sorted_inspections = sorted(monkey.inspect_counter for monkey in state.monkeys.values())
    return sorted_inspections[-1] * sorted_inspections[-2]


def read_input(state):
    for monkey_input in util.load_input_full(11).split("\n\n"):
        match = re.match(
            r"""Monkey (?P<index>\d+):
  Starting items: (?P<items>[0-9, ]+)
  Operation: (?P<operation>.*)
  Test: divisible by (?P<modulo>\d+)
    If true: throw to monkey (?P<to_true>\d+)
    If false: throw to monkey (?P<to_false>\d+)""",
            monkey_input
        )
        monkey = Monkey(
            index=int(match.group("index")),
            items=[int(x) for x in match.group("items").split(", ")],
            operation=eval(f"lambda old: {match.group('operation').removeprefix('new = ')}"),
            modulo=int(match.group("modulo")),
            throw_to_map={
                True: int(match.group("to_true")),
                False: int(match.group("to_false")),
            }
        )
        state.monkeys[monkey.index] = monkey


if __name__ == '__main__':
    main()
