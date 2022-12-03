# yeah so this is really shitty, I know I could do this more elegantly using a ring of 3 but :(
import enum

import util


class Move(enum.Enum):
    rock = enum.auto()
    paper = enum.auto()
    scissors = enum.auto()


def parse_move(code):
    match code:
        case "A" | "X":
            return Move.rock
        case "B" | "Y":
            return Move.paper
        case "C" | "Z":
            return Move.scissors


def match_result(their_move, your_move):
    print(their_move, your_move)
    move_score = {
        Move.rock: 1,
        Move.paper: 2,
        Move.scissors: 3
    }[your_move]
    if their_move == your_move:
        game_score = 3
    elif your_move == Move.rock and their_move == Move.scissors or your_move == Move.paper and their_move == Move.rock or your_move == Move.scissors and their_move == Move.paper:
        game_score = 6
    else:
        game_score = 0
    return move_score + game_score


def beats(winning_move):
    if winning_move == Move.rock:
        return Move.scissors
    if winning_move == Move.paper:
        return Move.rock
    if winning_move == Move.scissors:
        return Move.paper


def beats_reverse(losing_move):
    s = {Move.rock, Move.paper, Move.scissors}
    s.remove(losing_move)
    s.remove(beats(losing_move))
    return list(s)[0]


def p2_result(their_move, outcome):
    if outcome == Move.paper:  # draw
        return match_result(their_move, their_move)
    if outcome == Move.rock:  # lose
        return match_result(their_move, beats(their_move))
    # win
    return match_result(their_move, beats_reverse(their_move))


data = [[parse_move(move) for move in line.split()] for line in util.load_input(2)]

print("p1:", sum(match_result(*match_) for match_ in data))
print("p2:", sum(p2_result(*match_) for match_ in data))
