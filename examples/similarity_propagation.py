import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from simrank_cmp import compute_similarities

# Create a random graph
g = nx.grid_2d_graph(15, 15)
A = nx.adjacency_matrix(g).A

# For the initial similarity matrix, we assume every node is only similar to itself
sims = np.identity(len(g))

# Propagate the similarities using SimRank, using self loops
S = compute_similarities(A, A, sims, add_self_loops=True, decay=0.6)

# We want to color the nodes based on the similarity between them
# Because of the exponential decay factor, we take the log of the similarities for better visualization
intensities = np.log(S[len(g) // 2, :])
intensities = (intensities - intensities.min()) / intensities.ptp()
color_map = [plt.cm.Blues(intensity) for intensity in intensities]

# Show the results
plt.figure(figsize=(10,10))
layout = nx.nx_agraph.graphviz_layout(g, prog="dot")
nx.draw(g, layout, node_color=color_map, with_labels=True)
plt.show()
