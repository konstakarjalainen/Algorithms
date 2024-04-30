import sys

file_name = sys.argv[1]
starting_node = int(sys.argv[2])
file = open(file_name, "r")

graph = []
edges = {}
nodes = set()
for line in file:
    src, dest, w = line.split()
    src = int(src)
    dest = int(dest)
    nodes.add(src)
    nodes.add(dest)
    w = int(w)
    graph.append((src, dest, w))
    edges[(src, dest)] = w
graph.sort()
paths = {}
# i = 0
for node in nodes:
    if node == starting_node:
        paths[node] = (starting_node, 0)
    else:
        paths[node] = (None, float("inf"))
i = 1
is_negative_cycle = False
improved_nodes = [starting_node]
while i <= len(nodes):
    is_improvement = False
    looped_nodes = improved_nodes.copy()
    improved_nodes = []
    for node in looped_nodes:
        src_weight = paths[node][1]
        for edge in graph:
            src = edge[0]
            if src != node:
                continue
            dest = edge[1]
            weight = edge[2]
            if paths[dest][1] > src_weight + weight:
                is_improvement = True
                paths[dest] = (node, src_weight + weight)
                if dest not in improved_nodes:
                    improved_nodes.append(dest)
    if len(improved_nodes) > 0:
        improvement_str = f"Improvements in iteration {i}:"
        improved_nodes.sort()
        for node in improved_nodes:
            improvement_str = f"{improvement_str} d({node}) = {paths[node][1]},"
        print(improvement_str[:len(improvement_str)-1])
        if i == len(nodes):
            is_negative_cycle = True
    else:
        print(f"No improvements in iteration {i}")
        break
    i += 1
if is_negative_cycle:
    node = improved_nodes[0]
    for node in improved_nodes:
        cycle_cost = 0
        next_node = None
        cycle_nodes_arr = [node]
        first_round = True
        i = 0 
        while next_node not in cycle_nodes_arr:
            if first_round:
                next_node = node
            cycle_nodes_arr.append(next_node)
            first_round = False
            src = paths[next_node][0]
            cycle_cost += edges[(src, next_node)]
            next_node = src
            i += 1
        if cycle_cost < 0:
            cycle_string = f"{next_node}"
            node = None
            cost = 0
            while node != next_node:
                if node:
                    last_node = node
                else:
                    last_node = next_node
                node = cycle_nodes_arr.pop()
                cost += edges[(last_node, node)]
                cycle_string = f"{cycle_string} {node}"
            print(f"A negative cycle with cost {cost} detected: {cycle_string}")
            break
else:
    dist_str = ""
    for pair in paths.items():
        node = str(pair[0])
        value = str(pair[1][1])
        if value == "inf":
            value = "INF"
        dist_str = dist_str + ", d(" + node + ") = " + value
    print(f"Distances from {starting_node}:{dist_str[1:]}")

