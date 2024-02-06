'''My Calculator Test'''

from calculator import add, sub

def test_addition():
    '''Test that addition function works'''
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works'''
    assert sub(2,2) == 0
