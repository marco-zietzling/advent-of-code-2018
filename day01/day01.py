print("advent of code 2018 - day 1")

result = 0

with open("input.txt") as file:
    for line in file:
        result = result + int(line)

print("part 1: " + str(result))

