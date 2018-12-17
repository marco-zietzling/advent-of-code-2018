from PIL import Image
import numpy
from collections import defaultdict

print("advent of code 2018 - day 10")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 10 - part 1


# class Point:
#     x: int
#     y: int
#     vx: int
#     vy: int
#
#     def __init__(self, x: int, y: int, vx: int, vy: int):
#         self.x = x
#         self.y = y
#         self.vx = vx
#         self.vy = vy
#
#     def __repr__(self):
#         return f"Point({self.x}, {self.y}, {self.vx}, {self.vy})"


points = []
velocities = []

for line in lines:
    (x, y) = map(int, line.split("position=<")[1].split(">")[0].split(","))
    (vx, vy) = map(int, line.split("velocity=<")[1].split(">")[0].split(","))
    #point = Point(x=x, y=y, vx=vx, vy=vy)
    points.append((x, y))
    velocities.append((vx, vy))

# print(points)
# print(velocities)

counter = 0

min_x = min(points, key=lambda t: t[0])[0]
max_x = max(points, key=lambda t: t[0])[0]
min_y = min(points, key=lambda t: t[1])[1]
max_y = max(points, key=lambda t: t[1])[1]
canvas = defaultdict(bool)
for point in points:
    canvas[point] = True

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if canvas[(x, y)]:
            print("#", end="")
        else:
            print(".", end="")

    print("\n")

#image.save(f"image{counter:08}.png")

# canvas = [[-1 for x in range(-canvas_size, canvas_size)] for y in range(-canvas_size, canvas_size)]


