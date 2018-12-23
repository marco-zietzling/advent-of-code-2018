from collections import namedtuple

print("advent of code 2018 - day 23")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

Nanobot = namedtuple("Nanobot", "x y z radius")

nanobots = list()
nanobots_in_range = list()

for line in lines:
    x = int(line.split("<")[1].split(",")[0])
    y = int(line.split(",")[1])
    z = int(line.split(",")[2].split(">")[0])
    radius = int(line.split("r=")[1])

    nanobots.append(Nanobot(x=x, y=y, z=z, radius=radius))

# find strongest nanobot
max_radius = 0
strongest_nanobot = -1
for nanobot in nanobots:
    if nanobot.radius > max_radius:
        max_radius = nanobot.radius
        strongest_nanobot = nanobot

print(f"strongest nanobot: {strongest_nanobot}")

# find nanobots in range of strongest nanobot
for nanobot in nanobots:
    diff_x = abs(strongest_nanobot.x - nanobot.x)
    diff_y = abs(strongest_nanobot.y - nanobot.y)
    diff_z = abs(strongest_nanobot.z - nanobot.z)
    distance = diff_x + diff_y + diff_z
    if distance <= strongest_nanobot.radius:
        nanobots_in_range.append(nanobot)

print(f"part 1: {len(nanobots_in_range)}")
# 588



