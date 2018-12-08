print("advent of code 2018 - day 2")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

# day 2 - part 1
two_letters = 0
three_letters = 0

for line in lines:
    characters = {}
    found_two = False
    found_three = False

    for char in line:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    for x, y in characters.items():
        if y == 2:
            found_two = True
        if y == 3:
            found_three = True

    if found_two:
        two_letters += 1

    if found_three:
        three_letters += 1

print("part 1: " + str(two_letters * three_letters))
# 4980

# day 2 - part 2
with open("input.txt") as file:
    lines = [line.strip() for line in file]

for i in range(0, len(lines)):
    for j in range(i+1, len(lines)):

        num_different = sum(1 for a, b in zip(lines[i], lines[j]) if a != b)
        if num_different == 1:
            print("part 2: " + ''.join(list(a for a, b in zip(lines[i], lines[j]) if a == b)))

# qysdtrkloagnfozuwujmhrbvx
