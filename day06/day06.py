from collections import namedtuple

print("advent of code 2018 - day 6")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

coords = []
Coordinate = namedtuple('Coordinate', 'x y')
Distance = namedtuple('Distance', 'coord_index distance')

for line in lines:
    x, y = line.split(",")
    x, y = int(x), int(y)
    coords.append(Coordinate(x=x, y=y))

max_x = max(x for (x, _) in coords) + 1
max_y = max(y for (_, y) in coords) + 1

grid = [[-1 for x in range(max_x)] for y in range(max_y)]

for x in range(max_x):
    for y in range(max_y):
        distances = []

        for i in range(len(coords)):
            pos_x = coords[i].x
            pos_y = coords[i].y
            distance = abs(x - pos_x) + abs(y - pos_y)
            distances.append((i, distance))

        distances.sort(key=lambda t: t[1])

        if distances[0][1] != distances[1][1]:
            grid[x][y] = distances[0][0]
        else:
            print(grid[x][y])



print('\n'.join([''.join(['{:3}'.format(i) for i in row]) for row in grid]))
