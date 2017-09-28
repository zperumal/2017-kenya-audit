# opt.py
# Ronald L. Rivest
# September 26, 2017
# Code to test out ideas for Bayesian audits for Kenyan election


import numpy as np
import scipy.optimize


def find_A(x, y):
    """ Given nonnegative length-d real vectors x and y,
        return a "nice" matrix A such that Ax = y
        If x==y, return the d x d identity matrix.
        If x!=y, then we must have x!=0.
        Here "nice" means that A:
           (1) has nonnegative entries
           (2) has constant column sums
           (3) maximizes trace(A)
           (4) has 0 or constant values elsewhere
    """

    x = np.array(x)
    y = np.array(y)
    d = len(x)
    assert d == len(y)
    assert all(x >= 0)
    assert all(y >= 0)
    if all(x == y):
        return np.eye(d)
    if all(x==0):
        raise ValueError("find_A input error: x is zero but y != x: {} {}"
                         .format(x, y))
    scale = sum(y) / sum(x)
    A = find_A_2(scale*x, y)
    return scale*A
    # return np.around(result.x.reshape((d, d)), 2)


def find_A_2(x, y):
    """ Identical to find_A, except that we assume that
           (1) len(x) == len(y),
           (2) x != 0, and
           (2) sum(x) == sum(y).
        In this procedure we maximize the number of ballots that
        'stay the same'.
    """

    d = len(x)
    A = np.zeros((d, d))
    x_left = x.copy()
    y_togo = y.copy()
    for i in range(d):
        if x[i] != 0:
            kept = min(x[i], y[i])
            A[i, i] = kept / x[i]
            x_left[i] = x[i] - kept
            y_togo[i] = y[i] - kept
        else:
            A[i][i] = 1.0
    non_zeros = len([j for j in range(d) if np.around(y_togo[j], 5) != 0])
    for i in range(d):
        if x_left[i] != 0:
            for j in range(d):
                if j != i:
                    A[j][i] = y_togo[j] / (x[i] * non_zeros)
    return np.around(A, 5)


##############################################################################
## test routines for opt


def test_findA_once(x, y):
    A = find_A(x, y)
    print("\nfind_A: x={} y={} A=\n{}".format(x, y, A))
    print("y-Ax:", y-A.dot(x))

def test_findA():    
    test_findA_once([1, 4], [3, 2])
    test_findA_once([3, 2], [1, 4])
    test_findA_once([10, 10], [4, 16])
    test_findA_once([1, 2], [3, 0])
    test_findA_once([5, 5], [4, 4])
    test_findA_once([1, 5], [0, 6])
    test_findA_once([1, 2, 3], [1, 1, 4])
    test_findA_once([1, 1, 4, 4], [3, 3, 2, 2])
    test_findA_once([0, 0, 2, 2], [2, 2, 0, 0])
    test_findA_once([10, 10], [12, 8])
    test_findA_once([100, 100], [120, 80])
    test_findA_once([1000, 1000], [1200, 800])

if __name__ == "__main__":
    test_findA()

    
    
                                     
    
