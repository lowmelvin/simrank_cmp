import copy
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from simrank_sims import compute_similarities

def calculate_pairing(sims):
    """
    Given a similarity matrix, compute the most likely pairing of nodes
    """
    xs, ys = np.unravel_index(np.argsort(-sims, axis=None), sims.shape)
    seen_x, seen_y = set(), set()

    result = {}
    for x, y in zip(xs, ys):
        if x not in seen_x and y not in seen_y:
            result[x] = y
            seen_x.add(x)
            seen_y.add(y)

    return result

def calculate_accuracy(expected, predicted):
    """
    Given a dictionary of expected pairs and predicted pairs, compute the accuracy
    """
    correct = 0
    for x, y in expected.items():
        if x in predicted and predicted[x] == y:
            correct += 1

    return correct / len(expected)

# Create a random graph and a clone
f = nx.random_regular_graph(5, 124)
g = copy.deepcopy(f)
num_nodes = len(f)

# randomly shuffle the graph
expected = dict(zip(f.nodes(), sorted(f.nodes(), key=lambda k: random.random())))
g = nx.relabel_nodes(g, expected)

# For the initial similarity matrix, we assume a certain number of known matches
fraction_matched = 0.1
sims = np.zeros((num_nodes, num_nodes))
for i in range(int(num_nodes * fraction_matched)):
    sims[i, expected[i]] = 1

accuracies = []
for u, v in f.edges():
    f_adj = nx.adjacency_matrix(f, nodelist=list(range(num_nodes))).A
    g_adj = nx.adjacency_matrix(g, nodelist=list(range(num_nodes))).A

    sims_updated = compute_similarities(f_adj, g_adj, sims, add_self_loops=True, decay=0.8)
    predicted = calculate_pairing(sims_updated)
    accuracies.append(calculate_accuracy(expected, predicted))
    g.remove_edge(expected[u], expected[v])


# Graph accuracy against percent edges removed
ys = accuracies
xs = np.arange(len(ys)) / len(ys)
plt.figure(figsize=(10,10))
plt.plot(xs, ys, 'b-')

# Plot the baseline
plt.plot([0, 1], [fraction_matched, fraction_matched], 'r--')

# Add labels
plt.title('Node Matching Accuracy (10% Prelabeled)')
plt.xlabel('Fraction of Edges Removed')
plt.ylabel('Fraction of Nodes Matched')
plt.legend(['Accuracy', 'Baseline (Prelabeled Matches)'])

plt.show()
