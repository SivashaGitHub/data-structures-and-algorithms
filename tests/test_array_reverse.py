from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverseArray

def test_reverseArray1():
    assert  reverseArray([1,2,3,4,5]) == [5,4,3,2,1]

def test_reverseArray2():
    assert  reverseArray([10,20,30,40,50]) == [50,40,30,20,10]

def test_reverseArray3():
    assert  reverseArray([11,22,33,44,55]) == [55,44,33,22,11]

def test_reverseArray4():
    assert  reverseArray([12,22,32,42,52]) == [52,42,32,22,12]