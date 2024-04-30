import sys
from collections import deque


def MST(edges, s):
    edges_path = []
    mst = set()
    mst.add(s)
    prio_que = deque()
    total_cost = 0
    i = 1
    new_node_index = 1
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        if node1 == s or node2 == s:
            if len(prio_que) == 0:
                prio_que.append(edge)
            else:
                for j in range(len(prio_que)):
                    if prio_que[j][2] > edge[2] or (prio_que[j][2] == edge[2] and prio_que[j][0] > edge[0]) or (prio_que[j][2] == edge[2] and prio_que[j][0] == edge[0] and prio_que[j][1] > edge[1]):
                        prio_que.insert(j, edge)
                        break
                if j + 1 == len(prio_que):
                    prio_que.append(edge)
    while len(prio_que) > 0:
        
        print("** Iteration %d **" % (i))
        #print(prio_que)
        i += 1
        best_edge = prio_que.popleft()
        node1_new = best_edge[0] not in mst
        node2_new = best_edge[1] not in mst
        new_node_index = 0 if node1_new else 1
        new_node = best_edge[new_node_index]
        if node1_new or node2_new:
            print(f"Adding the edge {best_edge} with the new node {new_node}")
            mst.add(new_node)
            total_cost += best_edge[2]
            edges_path.append(best_edge)
            for edge in edges:
                if edge[0] == new_node and edge[1] not in mst or edge[1] == new_node and edge[0] not in mst:
                    #print(edge, prio_que)
                    for j in range(len(prio_que)):
                        if prio_que[j][2] > edge[2] or (prio_que[j][2] == edge[2] and prio_que[j][0] > edge[0]) or (prio_que[j][2] == edge[2] and prio_que[j][0] == edge[0] and prio_que[j][1] > edge[1]):
                            prio_que.insert(j, edge)
                            break
                    if j + 1 == len(prio_que):
                        prio_que.append(edge)
    return total_cost, sorted(edges_path)

file_name = sys.argv[1]
starting_node = int(sys.argv[2])
file = open(file_name, "r")
    
all_edges = [] # tuple (node1, node1, weight)
for line in file:
    n1, n2, w = line.split()
    all_edges.append((int(n1), int(n2), int(w)))

cost, edges = MST(all_edges, starting_node)
mst_string = ""

#print(edges)
for edge in edges:
    mst_string = mst_string + " " + str(edge[0]) + "-" + str(edge[1])  

 
print(f"MST({cost}):{mst_string}")
