# Exact Non-Iterative SimRank
Given two undirected graphs $F$ and $G$ and an initial similarity matrix $S_0$, SimRank propagates the similarity via the recurrence:
$$S = cF_{adj}^\top SG_{adj}+ S_0$$
where $c$ is a damping or decay factor between 0 and 1. Here the _adj_ matrices are the column-normalized adjacency matrices of the graphs.

The recurrence can be rewritten as an infinite sum, i.e.,
$$S = \sum_{k=0}^{\infty} c^k F_{adj}^{\top k} S_0 G_{adj}^k$$

Because $F$ and $G$ are undirected, the adjacency matrices are symmetric which implies that they are diagonalizable. It follows that the column-normalized versions are also diagonalizable, because the normalization can be written as a product of the original symmetric matrix and a positive-definite diagonal matrix (assuming no orphaned nodes).

We eigendecompose the matrices as follows:
$$
\begin{aligned}
F_{adj}^\top &= P_F D_F P_F^{-1} \\
G_{adj} &= P_G D_G P_G^{-1} 
\end{aligned}
$$
Solving,

$$
\begin{aligned}
S &= \sum_{k=0}^{\infty} c^kF_{adj}^{\top k} S_0 G_{adj}^k \\
&= \sum_{k=0}^{\infty} c^k(P_F D_F P_F^{-1})^{k} S_0 (P_G D_G P_G^{-1})^k \\
&= \sum_{k=0}^{\infty} c^k P_F D_F^k P_F^{-1} S_0 P_G D_G^k P_G^{-1} \\
&= P_F \left( \sum_{k=0}^{\infty} c^k D_F^k P_F^{-1} S_0 P_G D_G^k \right) P_G^{-1} \\
&= P_F \left( \sum_{k=0}^{\infty} (c \cdot {eigs}_F \cdot {eigs}_G^\top)^k \odot (P_F^{-1} S_0 P_G)  \right) P_G^{-1} 
\end{aligned}
$$

where ${eigs}_F$ and ${eigs}_G$ are column vectors corresponding to the diagonals of $D_F$ and $D_G$, respectively. Note that, because the adjacency matrices are column-normalized and $0 < c < 1$, we have $|c\lambda_F\lambda_G| < 1$ for any eigenvalue $\lambda_F$ of $F_{adj}$ and $\lambda_G$ of $G_{adj}$.

Thus, the last equation contains the sum of an infinite geometric series, where $c \cdot {eigs}_F \cdot {eigs}_G^\top$ is the common ratio. Rewriting one last time, we arrive at the final form:

$$
\begin{aligned}
R &= c \cdot {eigs}_F \cdot {eigs}_G^\top \\
A &= P_F^{-1} S_0 P_G \\
S &= P_F(A \oslash (1-R))P_G^{-1}
\end{aligned}
$$
