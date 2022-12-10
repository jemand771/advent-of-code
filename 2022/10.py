import util

current_cycle = 0
register_x = 1
p1_sum = 0
pixels = []


def inc_cycle():
    global current_cycle, p1_sum
    draw()
    current_cycle += 1
    if current_cycle in range(20, 221, 40):
        p1_sum += register_x * current_cycle


def draw():
    draw_target = current_cycle % 40
    pixels.append(abs(draw_target - register_x) <= 1)


for line in util.load_input(10):

    if line == "noop":
        inc_cycle()
        continue
    cmd, arg = line.split()
    if cmd == "addx":
        inc_cycle()
        inc_cycle()
        register_x += int(arg)

print("p1:", p1_sum)
for i, x in enumerate(pixels):
    print("##" if x else "  ", end="")
    if i % 40 == 39:
        print()
