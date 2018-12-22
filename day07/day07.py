print("advent of code 2018 - day 7")

with open("input.txt") as file:
    lines = [line.strip() for line in file]

nodes = set()
order = list()
result = list()

for line in lines:
    node1 = line.split(" ")[1]
    node2 = line.split(" ")[7]
    nodes.add(node1)
    nodes.add(node2)
    order.append((node1, node2))

# find first nodes without precondition
available_nodes = nodes - set(node for (_, node) in order)

# browse graph
while available_nodes:
    current_node = min(available_nodes)
    available_nodes.remove(current_node)
    result.append(current_node)
    print("".join(result))

    candidates = set(n2 for (n1, n2) in order if n1 == current_node)
    for candidate in candidates:
        if not set(n1 for (n1, n2) in order if n2 == candidate) - set(result):
            available_nodes.add(candidate)

print("part 1: " + "".join(result))
