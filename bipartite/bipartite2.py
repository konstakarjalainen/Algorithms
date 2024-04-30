import sys

filename = sys.argv[1]

file = open(filename, 'r')
edges = {}
edges_dest = {}
src_nodes = set()
dest_nodes = set()
for line in file:
    src, dest = line.split()
    src = int(src)
    dest = int(dest)
    src_nodes.add(src)
    dest_nodes.add(dest)
    if src in edges:
        edges[src].append(dest)
    else:
        edges[src] = [dest]
    if dest in edges_dest:
        edges_dest[dest].append(src)
    else:
        edges_dest[dest] = [src]

#print(len(src_nodes))
#print(len(dest_nodes))


def sort_edges(used_dest_nodes, edges):
    sorted_edges = {}
    max_size = 0
    for from_node, to_nodes in edges.items():
        to_nodes = [x for x in to_nodes if x not in used_dest_nodes]
        options_size = len(to_nodes)
        if max_size < options_size:
            max_size = options_size
        if options_size in sorted_edges:
            sorted_edges[options_size][from_node] = to_nodes
        else:
            sorted_edges[options_size] = {from_node: to_nodes}
    return sorted_edges, max_size



sources = []
destinations = []
sorted_edges, max_size = sort_edges(destinations, edges)
print(sorted_edges)
i = 1
while i <= max_size:
    added_pair = False
    if i in sorted_edges:

        for src, dests in sorted_edges[i].items():
            if i == 1:
                dest = dests[0]
                if dest not in destinations:
                    added_pair = True
                    sources.append(src)
                    destinations.append(dest)
                    del edges[src]
                    del edges_dest[dest]
                    edge_removed = False
                    for edge in edges.copy():
                        if dest in edges[edge]:
                            edge_removed = True
                            edges[edge].remove(dest)
                            if len(edges[edge]) == 0:
                                del edges[edge]
                    for edge in edges_dest.copy():
                        if src in edges_dest[edge]:
                            edges_dest[edge].remove(src)
                            if len(edges_dest[edge]) == 0:
                                del edges_dest[edge]
                break

            else:
                least_sources_dest = None
                least_sources_dest_len = float("inf")
                if src in edges:
                    for dest in dests:
                        if dest not in destinations:
                            if least_sources_dest_len > len(edges_dest[dest]):
                                least_sources_dest = dest
                                least_sources_dest_len = len(edges_dest[dest])
                if least_sources_dest is not None:
                    added_pair = True
                    sources.append(src)
                    destinations.append(least_sources_dest)
                    del edges[src]
                    del edges_dest[least_sources_dest]
                    for edge in edges.copy():
                        if dest in edges[edge]:
                            edges[edge].remove(dest)
                            if len(edges[edge]) == 0:
                                del edges[edge]
                    for edge in edges_dest.copy():
                        if src in edges_dest[edge]:
                            edges_dest[edge].remove(src)
                            if len(edges_dest[edge]) == 0:
                                del edges_dest[edge]
                    break
            
    if added_pair:
        sorted_edges, max_size = sort_edges(destinations, edges)
        i = 1
    else:
        i += 1

print(edges)
print(edges_dest)
print(sorted_edges)
#print(f"Number of unmatched src nodes: {len(src_nodes)-len(sources)}")
print(f"A maximum bipartite matching with {len(sources)} pairs:")
for i in range(len(sources)):
    print(f"{sources[i]} {destinations[i]}")