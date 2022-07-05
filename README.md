# SimRank-CMP

This is an implementation of SimRank for comparing small, undirected graphs. Notably, it can be used for augmenting pairwise similarities calculated using just the node labels alone, with structural similarity information from the edges.

The algorithm used is exact and non-iterative, and is based on a matrix formulation of SimRank. The main complexity comes from calculating the full eigen-decomposition of the adjacency matrices and then doing matrix multiplication. As such, it is not meant to be used on graphs much larger than a few thousand nodes. A derivation can be found [here](https://github.com/rzqx/simrank_cmp/blob/master/assets/explain.pdf).

For larger graphs and where 1) you don't need exact results, or 2) you don't need pairwise similarities, only similarities for specific node-pair s, there are alternative algorithms.

## Installation and Usage

Install with `pip install simrank-cmp`.

Usage is straightforward:

```
from simrank_cmp import compute_similarities

updated_similarities = compute_similarities(f_adj, g_adj, initial_similarities, decay=0.8)
```

`initial_similarities` should be the pairwise node similarities calculated using some other metric (such as Jaccard). It is important for there to be some signal here in this matrix; SimRank will propagate this information across the graphs.

## Examples

In `examples/similarity_propagation.py`, we visualize the propagation of similarity information across the graph from a single node (the center one in this picture). Darker means more similar.

![propagation](https://github.com/rzqx/simrank_cmp/blob/master/assets/similarity_propagation.png)

In `examples/match_robustness.py`, we show how the graph structure can help us match more nodes than just using the pairwise node similarities alone. In this example, only 10% of the nodes are labeled, but the algorithm is able to match 100% of the nodes when considering the graph structure. As edges are removed, accuracy drops as expected until we hit the baseline of 10%.






