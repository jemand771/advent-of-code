# TODO this is pretty shitty because you have to run it from the 2022 dir

def load_input_full(day):
    with open(f"inputs/{day}.txt", encoding="utf-8") as f:
        return f.read()


def load_input(day):
    return load_input_full(day).splitlines()


def load_input_single_line(day):
    line, *_ = load_input(day)
    return line
