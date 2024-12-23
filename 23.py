import networkx as nx

with open('input/23.txt', 'r') as f:
    lines = f.read().splitlines()

G = nx.Graph()
for line in lines:
    a, b = line.split('-')
    G.add_edge(a,b)

# find sets of 3 nodes that are connected
cliques = []
for clique in nx.enumerate_all_cliques(G):
    if len(clique) < 3:
        continue
    if len(clique) > 3:
        break
    if any([e.startswith('t') for e in clique]):
        cliques.append(clique)

print("Part 1:", len(cliques))

password = ",".join(sorted(nx.max_weight_clique(G, weight=None)[0]))

print("Part 2:", password)