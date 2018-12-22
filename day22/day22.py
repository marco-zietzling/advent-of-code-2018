from collections import namedtuple

print("advent of code 2018 - day 22")

with open("input.txt") as file:
    lines = [line.strip() for line in file]
    depth = int(lines[0].split(":")[1])
    target_x = int(lines[1].split(":")[1].split(",")[0])
    target_y = int(lines[1].split(":")[1].split(",")[1])

print(f"cave depth: {depth}, target coordinates: ({target_x}, {target_y})")

Region = namedtuple("Region", "x y geological_index erosion_level")

# constants
rocky = 0
wet = 1
narrow = 2

grid = [[Region(x=x, y=y, geological_index=-1, erosion_level=-1) for y in range(target_y + 1)] for x in range(target_x + 1)]

geological_index_grid = [[-1 for y in range(target_y + 1)] for x in range(target_x + 1)]
erosion_level_grid = [[-1 for y in range(target_y + 1)] for x in range(target_x + 1)]
region_type_grid = [[-1 for y in range(target_y + 1)] for x in range(target_x + 1)]

#prepare geological index
geological_index_grid[0][0] = 0
geological_index_grid[target_x][target_y] = 0
for x in range(target_x + 1):
    geological_index_grid[x][0] = x * 16807
for y in range(target_y + 1):
    geological_index_grid[0][y] = y * 48271


def print_grid(grid):
    for y in range(target_y + 1):
        for x in range(target_x + 1):
            print("{0:8d}".format(grid[x][y]), end="")
        print("")


#print_grid(geological_index_grid)
#print_grid(erosion_level_grid)
#print_grid(region_type_grid)

def get_geological_index(x: int, y: int):
    if x == 0 and y == 0:
        return 0
    if x == target_x and y == target_y:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271

    return get_erosion_level(x-1, y) * get_erosion_level(x, y-1)


def get_erosion_level(x: int, y: int):
    geological_index = get_geological_index(x, y)
    return (geological_index + depth) % 20183


def get_region_type(x: int, y: int):
    return get_erosion_level(x, y) % 3



# calculating geological index
#grid[0][0] = Region(x=0, y=0, geological_index=0, erosion_level=)