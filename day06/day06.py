from collections import namedtuple

print("advent of code 2018 - day 6")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 6 - part 1
coords = []
areas = {}
Coordinate = namedtuple('Coordinate', 'x y')
Distance = namedtuple('Distance', 'coord_index distance')

for line in lines:
    x, y = line.split(",")
    x = int(x)
    y = int(y)
    coords.append(Coordinate(x=x, y=y))

max_x = max(x for (x, _) in coords) + 1
max_y = max(y for (_, y) in coords) + 1

grid = [[99 for x in range(max_x)] for y in range(max_y)]
for current_coord_index in range(len(coords)):
    areas[current_coord_index] = 0

for x in range(max_x):
    for y in range(max_y):
        distances = []

        for current_coord_index in range(len(coords)):
            pos_x = coords[current_coord_index].x
            pos_y = coords[current_coord_index].y
            distance = abs(x - pos_x) + abs(y - pos_y)
            distances.append(Distance(coord_index=current_coord_index, distance=distance))

        distances.sort(key=lambda t: t.distance)

        if distances[0].distance != distances[1].distance:
            grid[x][y] = distances[0].coord_index
            areas[distances[0].coord_index] += 1
        else:
            grid[x][y] = -1


with open("result.txt", mode="w") as file:
    file.write('\n'.join([''.join(['{:3}'.format(i) for i in row]) for row in grid]))

for x in range(max_x):
    areas[grid[x][0]] = -1
    areas[grid[x][max_y - 1]] = -1

for y in range(max_y):
    areas[grid[0][y]] = -1
    areas[grid[max_x - 1][y]] = -1

print("part 1: " + str(max(areas.values())))
# 5975

