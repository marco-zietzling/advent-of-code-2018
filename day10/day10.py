from collections import namedtuple

print("advent of code 2018 - day 10")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 10 - part 1
points = []
velocities = []

for line in lines:
    (x, y) = map(int, line.split("position=<")[1].split(">")[0].split(","))
    (vx, vy) = map(int, line.split("velocity=<")[1].split(">")[0].split(","))
    points.append((x, y))
    velocities.append((vx, vy))


def calculate_dimensions(points):
    min_x = min(points, key=lambda t: t[0])[0]
    max_x = max(points, key=lambda t: t[0])[0]
    min_y = min(points, key=lambda t: t[1])[1]
    max_y = max(points, key=lambda t: t[1])[1]

    return max_x - min_x, max_y - min_y


counter = 0
(min_diff_x, min_diff_y) = calculate_dimensions(points)

while True:
    for i in range(len(points)):
        (x, y) = points[i]
        (vx, vy) = velocities[i]
        points[i] = (x + vx, y + vy)

    counter += 1

    (diff_x, diff_y) = calculate_dimensions(points)

    if diff_x <= min_diff_x and diff_y <= min_diff_y:
        min_diff_x = diff_x
        min_diff_y = diff_y
        print(f"step: {counter} dimensions: {diff_x} by {diff_y}")
    else:
        break

grid = [["." for y in range(min_diff_y + 1)] for x in range(min_diff_x + 1)]

# undo last step
counter -= 1
for i in range(len(points)):
    (x, y) = points[i]
    (vx, vy) = velocities[i]
    points[i] = (x - vx, y - vy)

# shift all points towards origin
offset_x = min(points, key=lambda t: t[0])[0]
offset_y = min(points, key=lambda t: t[1])[1]

for i in range(len(points)):
    (x, y) = points[i]
    points[i] = (x - offset_x, y - offset_y)

for i in range(len(points)):
    (x, y) = points[i]
    grid[x][y] = "#"

print("day 10 - part 1")
for y in range(min_diff_y + 1):
    for x in range(min_diff_x + 1):
        print(grid[x][y], end="")

    print("")

print("day 10 - part 2")
print(f"#steps = {counter}")
# 10656
