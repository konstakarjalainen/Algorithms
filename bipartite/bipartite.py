import sys

class GFG:
    def __init__(self,graph):
        self.graph = graph
        self.sources = len(graph)
        self.dests = len(graph[0])
    
    def bpm(self, u, matchR, seen):
        for v in range(self.dests):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True

                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False
    
    def maxBPM(self):
        matchR = [-1] * self.dests
        result = 0
        for i in range(self.sources):

            seen = [False] * self.dests

            if self.bpm(i, matchR, seen):
                result += 1
        return result, matchR


filename = sys.argv[1]

file = open(filename, 'r')
edges = []
src_nodes = set()
dest_nodes = set()
for line in file:
    src, dest = line.split()
    src = int(src)
    dest = int(dest)
    src_nodes.add(src)
    dest_nodes.add(dest)
    edges.append((src, dest))

graph = []
src_nodes = list(src_nodes)
dest_nodes = list(dest_nodes)
i = 0
for src in src_nodes:
    graph.append([])
    for dest in dest_nodes:
        if (src,dest) in edges:
            graph[i].append(1)
        else:
            graph[i].append(0)
    i += 1

g = GFG(graph)
max_pairs, matches = g.maxBPM()
print(f"A maximum bipartite matching with {max_pairs} pairs:")
for i in range(len(matches)): 
    if matches[i] != -1:
        print(f"{src_nodes[matches[i]]} {dest_nodes[i]}")