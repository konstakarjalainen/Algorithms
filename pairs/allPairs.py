import sys


def find_neg_cycle(start_node, spEdge):
    print(start_node+1, end="")
    next_node = spEdge[start_node][start_node][1]
    print(f" {next_node}", end="")
    while next_node != start_node+1:
        next_node = spEdge[next_node-1][start_node][1]
        print(f" {next_node}", end="")
    print()


filename = sys.argv[1]

file = open(filename, "r")

edges = {}
all_nodes = set()
for line in file:
    src, dest, w = line.split()
    src = int(src)
    dest = int(dest)
    w = int(w)
    all_nodes.add(src)
    all_nodes.add(dest)
    edges[(src, dest)] = w

num_nodes = len(all_nodes)
spEdge = [["null" for _ in range(num_nodes)] for _ in range(num_nodes)]
D = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
D_row_format = "{:>5}" * num_nodes
edge_row_format = "{:>7}" * num_nodes
for i in range(1, num_nodes + 1):
    for j in range(1, num_nodes + 1):
        if (i,j) in edges:
            D[i-1][j-1] = edges[(i, j)]
            spEdge[i-1][j-1] = (i, j)
        else:
            D[i-1][j-1] = float("inf")
    D[i-1][i-1] = 0
print("Iteration 0")      
for d in range(num_nodes):
    print(D_row_format.format(*D[d]))
print()
for sp in range(num_nodes):
    row = spEdge[sp].copy()
    for val_i in range(len(row)):
        if row[val_i] != "null":
            row[val_i] = f"{row[val_i][0]}-{row[val_i][1]}"
    print(edge_row_format.format(*row))
print()
for k in range(1, num_nodes + 1):
    print(f"Iteration {k}")
    for i in range(1, num_nodes + 1):
        for j in range(1, num_nodes + 1):
            if D[i-1][j-1] > D[i-1][k-1] + D[k-1][j-1]:
                D[i-1][j-1] = D[i-1][k-1] + D[k-1][j-1]
                spEdge[i-1][j-1] = spEdge[i-1][k-1]
    for d in range(num_nodes):
        print(D_row_format.format(*D[d]))
    print()
    for sp in range(num_nodes):
        row = spEdge[sp].copy()
        for val_i in range(len(row)):
            if row[val_i] != "null":
                row[val_i] = f"{row[val_i][0]}-{row[val_i][1]}"
        print(edge_row_format.format(*row))
    print()
    for i in range(num_nodes):
        neg_cycle = False
        if D[i][i] < 0:
            print("A negative cycle detected: ", end="")
            find_neg_cycle(i, spEdge)
            neg_cycle = True
            break
    if neg_cycle:
        break
