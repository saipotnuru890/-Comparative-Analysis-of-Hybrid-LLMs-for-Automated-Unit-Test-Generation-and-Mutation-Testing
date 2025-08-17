# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 00:00:12 2025

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 23:29:11 2025

@author: HP
"""

import pytest
from math_operations1 import add, multiply, is_even

def test_add():
    # Basic cases
    assert add(0, 0) == 0
    assert add(1, 1) == 2
    assert add(-1, -1) == -2
    assert add(48, 48) == 96

    # Large numbers
    assert add(100000, 200000) == 300000
    assert add(-100000, -200000) == -300000  

    # Edge cases
    assert add(-50, 50) == 0  # Opposite numbers
    assert add(2147483647, 1) == 2147483648  # Integer overflow boundary
    assert add(-2147483648, -1) == -2147483649  # Negative overflow
    assert add(0, 0) == 0, "Zero addition failed!"
    assert add(1, 1) == 2, "Positive number addition failed!"
    assert add(-1, -1) == -2, "Negative number addition failed!"
    assert add(48, 48) == 96, "Equal number addition failed!"
    assert add(100000, 200000) == 300000, "Large number addition failed!"
    assert add(-50, 50) == 0, "Opposite numbers failed!"
    assert add(3.5, 2.5) == 6.0, "Float addition failed!"

def test_is_even():
    # Basic cases
    assert is_even(0) == True
    assert is_even(1) == False
    assert is_even(-1) == False
    assert is_even(20) == True

    # Large numbers
    assert is_even(999999) == False  
    assert is_even(1000000) == True  

    # Edge cases
    assert is_even(-2) == True  # Negative even number
    assert is_even(-999999) == False  # Large negative odd number
    assert is_even(2**30) == True  # Large power of 2
    assert is_even((2**30) - 1) == False  # Large odd number

def test_multiply():
    # Basic cases
    assert multiply(0, 0) == 0
    assert multiply(1, 1) == 1
    assert multiply(-1, -1) == 1
    assert multiply(67, 51) == 3417

    # Large numbers
    assert multiply(10**6, 10**6) == 10**12  
    assert multiply(-10**6, 10**6) == -10**12  
    assert multiply(-10**6, -10**6) == 10**12  

    # Edge cases
    assert multiply(1, 0) == 0  # Multiplication with zero
    assert multiply(-5, 5) == -25  
    assert multiply(2**31 - 1, 1) == 2**31 - 1  # Max positive int
    assert multiply(-2**31, 1) == -2**31  # Min negative int
    assert multiply(0, 10) == 0, "Multiplication with zero failed!"
    assert multiply(1, 100) == 100, "Multiplication by one failed!"
    assert multiply(-2, 3) == -6, "Negative multiplication failed!"
    assert multiply(-5, -5) == 25, "Negative-negative multiplication failed!"
    assert multiply(10**6, 10**6) == 10**12, "Large number multiplication failed!"
    assert multiply(0.5, 2) == 1.0, "Float multiplication failed!"

def test_invalid_inputs():
    with pytest.raises(TypeError):
        add("a", 1)  # String and int
    with pytest.raises(TypeError):
        add(None, 5)  # None and int
    with pytest.raises(TypeError):
        add([1, 2], 3)  # List and int

    with pytest.raises(TypeError):
        multiply(3.5, "test")  # Float and string
    with pytest.raises(TypeError):
        multiply(None, 5)  # None and int
    with pytest.raises(TypeError):
        multiply({}, 5)  # Dict and int

    with pytest.raises(TypeError):
        is_even("string")  # String input
    with pytest.raises(TypeError):
        is_even(None)  # None input
    with pytest.raises(TypeError):
        is_even(3.5)  # Float input
    with pytest.raises(TypeError):
        add("a", 1)  # String + Int
    with pytest.raises(TypeError):
        add(None, 5)  # None + Int
    with pytest.raises(TypeError):
        multiply("string", 2)  # String * Int
    with pytest.raises(TypeError):
        is_even("text")  # Non-integer
    with pytest.raises(TypeError):
        is_even(3.5)  # Float should not be allowed
