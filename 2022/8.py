import util

# not proud of all the copy pasting for each direction that's going on here but I don't really know how to do it better.
# maybe using an array of hardcoded offsets like [[0, 1], [0, -1], [1, 0], [-1, 0]] ?

grid = [
    [int(tree) for tree in line]
    for line in util.load_input(8)
]
DIM_X = len(grid[0])
DIM_Y = len(grid)

visible = [[False] * DIM_X for _ in range(DIM_Y)]
scores = [[None] * DIM_X for _ in range(DIM_Y)]


def is_visible(x, y):
    if x == 0 or y == 0 or x == DIM_X - 1 or y == DIM_Y - 1:
        return True
    height = grid[y][x]
    if all(grid[y][ix] < height for ix in range(x)):
        return True
    if all(grid[y][ix] < height for ix in range(x + 1, DIM_X)):
        return True
    if all(grid[iy][x] < height for iy in range(y)):
        return True
    if all(grid[iy][x] < height for iy in range(y + 1, DIM_Y)):
        return True
    return False


def calc_score(x, y):
    dist_l = dist_r = dist_t = dist_b = 0
    height = grid[y][x]
    for xi in range(x - 1, -1, -1):
        dist_l += 1
        if grid[y][xi] >= height:
            break
    for xi in range(x + 1, DIM_X):
        dist_r += 1
        if grid[y][xi] >= height:
            break
    for yi in range(y - 1, -1, -1):
        dist_t += 1
        if grid[yi][x] >= height:
            break
    for yi in range(y + 1, DIM_Y):
        dist_b += 1
        if grid[yi][x] >= height:
            break

    return dist_l * dist_r * dist_t * dist_b


for y_ in range(DIM_Y):
    for x_ in range(DIM_X):
        vis = is_visible(x_, y_)
        visible[y_][x_] = vis
        scores[y_][x_] = calc_score(x_, y_)

print("p1:", sum(val for row in visible for val in row))
# don't yell at me this works
# noinspection PyTypeChecker
print("p2:", max(val for row in scores for val in row if val is not None))
