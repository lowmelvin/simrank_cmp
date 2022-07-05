# SimRank-CMP

This is an implementation of SimRank for comparing small, undirected graphs. Notably, it can be used for augmenting pairwise similarities calculated using just the node labels alone, with structural similarity information from the edges.

The algorithm used is exact and non-iterative, and is based on a matrix formulation of SimRank. The main complexity comes from calculating the full eigen-decomposition of the adjacency matrices and then doing matrix multiplication. As such, it is not meant to be used on graphs much larger than a few thousand nodes. A derivation can be found here:

## Installation and Usage

Install with `pip install simrank-cmp`.

Usage is straightforward:

```
from simrank_cmp import compute_similarities

updated_similarities = compute_similarities(f_adj, g_adj, initial_similarities, decay=0.8)
```

`initial_similarities` should be the pairwise node similarities calculated using some other metric (such as Jaccard).

## Examples





