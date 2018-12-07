print("advent of code 2018 - day 1")

# day 1 - part 1
frequency = 0

with open("input.txt") as file:
    for line in file:
        frequency = frequency + int(line)

print("part 1: " + str(frequency))

# day 1 - part 2
frequency = 0
frequencies = set()
loop = True

while loop:
    with open("input.txt") as file:
        for line in file:
            frequency = frequency + int(line)
            if frequency in frequencies:
                print("part 2: " + str(frequency))
                loop = False
                break
            else:
                frequencies.add(frequency)

