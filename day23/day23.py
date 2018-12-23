from collections import namedtuple

print("advent of code 2018 - day 23")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

Nanobot = namedtuple("Nanobot", "x y z radius")

nanobots = list()

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
in_range = list()
for nanobot in nanobots:
    diff_x = abs(strongest_nanobot.x - nanobot.x)
    diff_y = abs(strongest_nanobot.y - nanobot.y)
    diff_z = abs(strongest_nanobot.z - nanobot.z)
    distance = diff_x + diff_y + diff_z
    if distance <= strongest_nanobot.radius:
        in_range.append(nanobot)

nanobots_in_range = len(in_range)
print(f"part 1: {nanobots_in_range}")
# 588

# find dimensions of grid
min_x = min(x for (x, _, _, _) in nanobots)
max_x = max(x for (x, _, _, _) in nanobots)

min_y = min(y for (_, y, _, _) in nanobots)
max_y = max(y for (_, y, _, _) in nanobots)

min_z = min(z for (_, _, z, _) in nanobots)
max_z = max(z for (_, _, z, _) in nanobots)

max_number_of_nanobots_in_range = 0


def count_nanobots_in_range(x: int, y: int, z: int):
    in_range = list()
    for nanobot in nanobots:
        diff_x = abs(x - nanobot.x)
        diff_y = abs(y - nanobot.y)
        diff_z = abs(z - nanobot.z)
        distance = diff_x + diff_y + diff_z
        if distance <= nanobot.radius:
            in_range.append(nanobot)

    return len(in_range)


for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        for z in range(min_z, max_z):
            #print(f"{x} {y} {z}")

            nanobots_in_range = count_nanobots_in_range(x, y, z)
            #print(f"nanobots in range: {nanobots_in_range}")

            if nanobots_in_range > max_number_of_nanobots_in_range:
                max_number_of_nanobots_in_range = nanobots_in_range
                print(f"{max_number_of_nanobots_in_range}")


print(f"max number of nanobots in range: {max_number_of_nanobots_in_range}")

