from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test_insertShiftArray1():
    assert  insertShiftArray([4,8,15,23,42],16) == [4,8,15,16,23,42]

def test_insertShiftArray2():
    assert  insertShiftArray([2,4,6,8],5) == [2,4,5,6,8]

def test_insertShiftArray3():
    assert  insertShiftArray([11,22,33,44,55],23) == [11,22,23,33,44,55]

def test_insertShiftArray4():
    assert  insertShiftArray([12,22,32,42,52],43) == [12,22,32,42,43,52]

    