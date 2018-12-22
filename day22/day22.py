print("advent of code 2018 - day 22")

with open("input.txt") as file:
    lines = [line.strip() for line in file]
    depth = int(lines[0].split(":")[1])
    target_x = int(lines[1].split(":")[1].split(",")[0])
    target_y = int(lines[1].split(":")[1].split(",")[1])

print(f"cave depth: {depth}, target coordinates: ({target_x}, {target_y})")

# grids
geological_index_grid = [[-1 for _ in range(target_y + 1)] for _ in range(target_x + 1)]
erosion_level_grid = [[-1 for _ in range(target_y + 1)] for _ in range(target_x + 1)]
region_type_grid = [[-1 for _ in range(target_y + 1)] for _ in range(target_x + 1)]

# constants
rocky = 0
wet = 1
narrow = 2


def print_grid(grid):
    for y in range(target_y + 1):
        for x in range(target_x + 1):
            print("{0:8d}".format(grid[x][y]), end="")
        print("")


def get_geological_index(x: int, y: int):
    if geological_index_grid[x][y] == -1:
        calc_geological_index(x, y)

    return geological_index_grid[x][y]


def calc_geological_index(x: int, y: int):
    if x == 0 and y == 0:
        geological_index_grid[x][y] = 0
    elif x == target_x and y == target_y:
        geological_index_grid[x][y] = 0
    elif y == 0:
        geological_index_grid[x][y] = x * 16807
    elif x == 0:
        geological_index_grid[x][y] = y * 48271
    else:
        geological_index_grid[x][y] = get_erosion_level(x-1, y) * get_erosion_level(x, y-1)


def get_erosion_level(x: int, y: int):
    if erosion_level_grid[x][y] == -1:
        calc_erosion_level(x, y)

    return erosion_level_grid[x][y]


def calc_erosion_level(x: int, y: int):
    geological_index = get_geological_index(x, y)
    erosion_level_grid[x][y] = (geological_index + depth) % 20183


def get_region_type(x: int, y: int):
    if region_type_grid[x][y] == -1:
        calc_region_type(x, y)

    return region_type_grid[x][y]


def calc_region_type(x: int, y: int):
    region_type_grid[x][y] = get_erosion_level(x, y) % 3


result = 0
for y in range(target_y + 1):
    for x in range(target_x + 1):
        result += get_region_type(x, y)

# print("geological index grid")
# print_grid(geological_index_grid)
# print("erosion level grid")
# print_grid(erosion_level_grid)
# print("region type grid")
# print_grid(region_type_grid)
print(f"part 1: {result}")
#8575


