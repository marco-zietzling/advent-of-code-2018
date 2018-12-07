print("advent of code 2018 - day 3")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 3 - part 1

matrix = [[0 for x in range(1000)] for y in range(1000)]
counter = 0

for line in lines:
    line_id = int(line.split("#")[1].split("@")[0])
    pos_x = int(line.split("@")[1].split(",")[0])
    pos_y = int(line.split(",")[1].split(":")[0])
    len_x = int(line.split(":")[1].split("x")[0])
    len_y = int(line.split("x")[1])

    for i in range(pos_x, pos_x + len_x):
        for j in range(pos_y, pos_y + len_y):
            if matrix[i][j] == 1:
                counter += 1

            matrix[i][j] += 1

print("part 1: " + str(counter))

#day 3 - part 2

