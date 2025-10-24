#TESTS
import pytest
from sievetools import *


#Testing for integer values
def test_slow_noninteger():
    with pytest.raises(TypeError):
        sieve_slow(0.5) # Making sure that a type error would be raised if a noninteger was placed in here

#Testing for edge case 2
def test_slow_2():
    output = sieve_slow(2)
    expected = [2]
    
    assert output == expected

#Testing for edge case 1
def test_slow_1():
    output = sieve_slow(1)
    expected = []
    
    assert output == expected

#Test for regular case outputs (interior test)
def test_slow_interior():
    output = sieve_slow(10)
    expected = [2, 3, 5, 7]
    
    assert output == expected