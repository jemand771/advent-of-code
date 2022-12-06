import util

line = util.load_input_single_line(6)

def find_marker(marker_len: int):
    for i, recent_chars in enumerate(zip(*(line[start:] for start in range(marker_len))), start=marker_len):
        if len(set(recent_chars)) == marker_len:
            return i

print("p1:", find_marker(4))
print("p2:", find_marker(14))
