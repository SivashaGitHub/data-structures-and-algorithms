from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch

def test_BinarySearch1():
    assert  BinarySearch([11,22,33,44,55,66,77], 90) == -1

def test_BinarySearch2():
    assert  BinarySearch([4,8,15,16,23,42], 15) == 2

def test_BinarySearch3():
    assert  BinarySearch([11,22,33,44,55],54) == -1

def test_BinarySearch4():
    assert  BinarySearch([12,22,32,42,52],42) == 3
