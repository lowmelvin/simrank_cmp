import unittest
from simrank_cmp import compute_similarities, col_norm_eigh
import numpy as np

class TestSimRank(unittest.TestCase):
    def test_eigh(self):
        # Create a random symmetric matrix
        A = np.random.rand(50, 50)
        A = A + A.T
        A_normed = A / np.sum(A, axis=0)

        # Calculate the eigenvalues and eigenvectors
        eigvals, eigvecs, inv = col_norm_eigh(A)

        for i, eigval in enumerate(eigvals):
            eigvec = eigvecs[:,i]
            self.assertTrue(np.allclose(A_normed@eigvec, eigval*eigvec))

        self.assertTrue(np.allclose(np.linalg.inv(eigvecs), inv))

    def test_simrank_basic(self):
        N = 50
        A = np.ones((N, N))
        S = np.ones((N, N))

        sims = compute_similarities(A, A, S, add_self_loops=False)
        
        # Output should be symmetric
        self.assertTrue(np.allclose(sims, sims.T))

        # Output should be different from start
        self.assertFalse(np.allclose(sims, S))

    def test_simrank_self_loops(self):
        N = 50
        A = np.zeros((N, N))
        S = np.ones((N, N))

        sims = compute_similarities(A, A, S, add_self_loops=True)
        
        # Output should be symmetric
        self.assertTrue(np.allclose(sims, sims.T))

        # Output should be different from start
        self.assertFalse(np.allclose(sims, S))

if __name__ == '__main__':
    unittest.main()
