import numpy as np

def _col_norm(matrix):
    return matrix / matrix.sum(axis=0)

def compute_similarities(f_adj, g_adj, sim_matrix, add_self_loops=True, decay=0.6):
    """
    Compute the similarities between the nodes of two undirected graphs using vanilla SimRank.
    :param f_adj: The adjacency matrix of the first graph.
    :param g_adj: The adjacency matrix of the second graph.
    :param sim_matrix: The intial similarity matrix.
    :param add_self_loops: Whether self-loops should be added to the adjacency matrices.
    :param decay: The decay factor.
    """
    if add_self_loops:
        np.fill_diagonal(f_adj, 1)
        np.fill_diagonal(g_adj, 1)
    
    f_adj_normed = _col_norm(f_adj).T
    g_adj_normed = _col_norm(g_adj)

    # matrices are no longer symmetric after column normalization!
    f_eigs, f_vecs = np.linalg.eig(f_adj_normed)
    g_eigs, g_vecs = np.linalg.eig(g_adj_normed)

    R = decay * (f_eigs[:,np.newaxis] @ g_eigs[np.newaxis,:]) 
    A = np.linalg.inv(f_vecs) @ sim_matrix @ g_vecs

    result = f_vecs @ (A / (1 - R)) @ np.linalg.inv(g_vecs)
    return result.real
