print("advent of code 2018 - day 5")

with open("input.txt") as file:
    lines = [line.strip() for line in file]


# day 5 - part 1
def get_character_list(input_string):
    return [i for i in input_string]


def react_polymer(items):
    change = True
    while change:
        change = False
        for i in range(len(items)):
            if i + 1 < len(items):
                if abs(ord(items[i]) - ord(items[i+1])) == 32:
                    del(items[i])
                    del(items[i])
                    change = True

    return items


characters = get_character_list(lines[0])
result = react_polymer(characters)

print("part 1: " + str(len(result)))
# 9526


# part 5 - part 2
def remove_values_from_list(input_list, value):
    return [v for v in input_list if v != value]


min_polymer_length = 99999

for i in range(ord('a'), ord('z')):
    uppercase_char = chr(i - 32)
    lowercase_char = chr(i)

    characters = get_character_list(lines[0])
    characters = remove_values_from_list(characters, uppercase_char)
    characters = remove_values_from_list(characters, lowercase_char)

    current_polymer_length = len(react_polymer(characters))

    print("removing " + lowercase_char + " and " + uppercase_char + " resulting in " + str(current_polymer_length))

    if current_polymer_length < min_polymer_length:
        min_polymer_length = current_polymer_length

print("part 2: " + str(min_polymer_length))
# 6694
