from dataclasses import dataclass
from typing import Optional

import util


@dataclass
class Pos:
    x: int = 0
    y: int = 0

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def as_signs(self):
        return Pos(
            0 if self.x == 0 else self.x // abs(self.x),
            0 if self.y == 0 else self.y // abs(self.y)
        )

    def as_tuple(self):
        return self.x, self.y


class State:
    head: Pos
    tail: Pos
    visited: set[tuple]
    child: Optional["State"]

    def __init__(self, child=None):
        self.head = Pos()
        self.tail = Pos()
        self.visited = {(0, 0)}
        self.child = child

    def apply_head(self, offset: Pos):
        self.head += offset
        self.snap_tail()
        if self.child is not None:
            self.child.head = self.tail
            # dummy operation, we've already set the thing
            self.child.apply_head(Pos())

    def snap_tail(self):
        offset = self.head - self.tail
        if abs(offset.x) <= 1 and abs(offset.y) <= 1:
            return
        if offset.x == 0:
            apply_offset = Pos(0, offset.y // abs(offset.y))
        elif offset.y == 0:
            apply_offset = Pos(offset.x // abs(offset.x), 0)
        else:
            apply_offset = offset.as_signs()
        self.tail += apply_offset
        self.visited.add(self.tail.as_tuple())
        self.snap_tail()


def main():
    first = State()
    last = first
    for _ in range(8):
        last.child = State()
        last = last.child
    for line in util.load_input(9):
        direction, count = line.split()
        count = int(count)
        offset = Pos(0, 0)
        match direction:
            case "U":
                offset += Pos(0, -count)
            case "D":
                offset += Pos(0, count)
            case "L":
                offset += Pos(-count, 0)
            case "R":
                offset += Pos(count, 0)
        for _ in range(count):
            # I don't know why this matters (just doing it in one move worked for all examples) but oh well.
            # the p2 answer from applying the offset directly is too low
            first.apply_head(offset.as_signs())
    print("p1:", len(first.visited))
    print("p2:", len(last.visited))  # 2581 is too low


if __name__ == '__main__':
    main()
