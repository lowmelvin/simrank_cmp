import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from simrank_cmp import compute_similarities

# Create a random graph
g = nx.full_rary_tree(3, 53)
A = nx.adjacency_matrix(g).A

# For the initial similarity matrix, we assume every node is similar to every other node
sims = np.ones(A.shape)

# Propagate the similarities using SimRank, using self loops
S = compute_similarities(A, A, sims, add_self_loops=True, decay=0.98)
diag = np.diag(S)
diag = np.round(np.log(diag), decimals = 5)

# Associate each unique value on the diagonal with a color
unique_values = np.unique(diag)
colors = { u: plt.cm.jet(i / len(unique_values)) for i, u in enumerate(unique_values) }
color_map = [colors[u] for u in diag]

# Show the results
plt.figure(figsize=(10,10))
layout = nx.nx_agraph.graphviz_layout(g, prog="dot")
nx.draw(g, layout, node_color=color_map, with_labels=True)
plt.show()
