from PIL import Image

print("advent of code 2018 - day 10")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 10 - part 1


class Point:
    x: int
    y: int
    vx: int
    vy: int

    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.vx}, {self.vy})"


points = []

for line in lines:
    x, y = map(int, line.split("position=<")[1].split(">")[0].split(","))
    vx, vy = map(int, line.split("velocity=<")[1].split(">")[0].split(","))
    point = Point(x=x, y=y, vx=vx, vy=vy)
    points.append(point)

# print(points)



# canvas_size = 56000
# canvas = [[-1 for x in range(-canvas_size, canvas_size)] for y in range(-canvas_size, canvas_size)]


