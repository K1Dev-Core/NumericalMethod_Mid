import numpy as np

def cramers_rule(A, b):
    """
    Cramer's Rule for solving Ax = b (square system)
    x_i = det(A_i) / det(A)
    where A_i is A with column i replaced by b.

    Note:
    - Works best for small systems (2x2, 3x3, 4x4).
    - If det(A) = 0, the system has no unique solution.
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1)

    n, m = A.shape
    if n != m:
        raise ValueError("A must be a square matrix.")
    if b.size != n:
        raise ValueError("b must have the same number of rows as A.")

    detA = np.linalg.det(A)
    if abs(detA) == 0:
        raise ValueError("det(A)=0 -> no unique solution (cannot use Cramer's rule).")

    x = np.zeros(n, dtype=float)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        x[i] = np.linalg.det(Ai) / detA

    return x, detA

if __name__ == "__main__":
    # Example (3x3)
    # 2x +  y -  z =  8
    # -3x - y + 2z = -11
    # -2x + y + 2z = -3
    A = [
        [ 2,  1, -1],
        [-3, -1,  2],
        [-2,  1,  2],
    ]
    b = [8, -11, -3]

    x, detA = cramers_rule(A, b)

    print("det(A) =", detA)
    print("Solution (x, y, z) =", x)
