#from matrix_sum import __version__
from data_structures_and_algorithms.challenges.matrix_sum.matrix_sum import sum_matrix_fn,sum_matrix_using_sum_fn


# def test_get_matrix():

def test_summed_matrix1():
    assert  sum_matrix_fn([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]) ==[6, 15, 18]
  
def test_summed_matrix2():
    assert  sum_matrix_fn([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ]) ==[6, 5, 20]

def test_summed_matrix3():
    assert  sum_matrix_using_sum_fn([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]) ==[6, 15, 18]

def test_summed_matrix3():
    assert  sum_matrix_using_sum_fn([ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ]) ==[6, 5, 20]

