import sys

filename = sys.argv[1]

file = open(filename, "r")
src_nodes = set()
dest_nodes = set()
edges = {}
for line in file:
    src, dest = line.split()
    src = int(src)
    dest = int(dest)
    dest_nodes.add(dest)
    src_nodes.add(src)
    if dest in edges:
        edges[dest].append(src)
    else:
        edges[dest] = [src]
to_remove = []
for src_node in src_nodes:
    if src_node in dest_nodes:
        to_remove.append(src_node)
for node in to_remove:
    src_nodes.remove(node)
src_nodes = sorted(src_nodes)
dest_nodes = sorted(dest_nodes)
order = []
cycle_found = False
while len(src_nodes) > 0:
    node = src_nodes[0]
    if node not in dest_nodes:
        found_source_node = True
        src_nodes.remove(node)
        order.append(node)
        to_delete = [] 
        for pair in edges.items():
            if node in pair[1]:
                pair[1].remove(node)
                if len(pair[1]) == 0 and pair[0] not in src_nodes:
                    to_delete.append(pair[0])
        for dest_node in to_delete:
            del edges[dest_node]
            dest_nodes.remove(dest_node)
            src_nodes.append(dest_node)
        src_nodes.sort()
    if len(src_nodes) == 0 and len(dest_nodes) > 0:
        cycle_found = True
        break

to_print = ""
if cycle_found:
    prev_node = dest_nodes[0]
    cycle_order =  [prev_node]
    cycle = False
    while not cycle:
        next_node = min(edges[prev_node])
        if next_node in cycle_order:
            cycle = True
        cycle_order.append(next_node)
        prev_node = next_node
    cycle_order.reverse()
    first_node = cycle_order[0]
    i = 0
    for node in cycle_order:
        to_print = to_print + " " + str(node)
        if node == first_node and i != 0:
            break
        i += 1
    print(f"The graph is not acyclic, found a cycle:{to_print}")
else: 
    for node in order:
        to_print = to_print + " " + str(node)
    print(f"Found a topological order:{to_print}")
