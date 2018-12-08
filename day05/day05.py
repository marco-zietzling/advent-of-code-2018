print("advent of code 2018 - day 5")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

items = []

for i in lines[0]:
    items.append(i)

print(len(items))

change = True
while change:
    change = False
    for i in range(len(items)):
        if i + 1 < len(items):
            if abs(ord(items[i]) - ord(items[i+1])) == 32:
                # print("match found: " + items[i] + items[i+1])
                del(items[i])
                del(items[i])
                change = True

print("part 1: " + str(len(items)))
# 9526

