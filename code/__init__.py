# content of __init__.py
# simple testing script to determine if travis is working

def square(x):
    return x * x

def test_square():
    assert square(2) == 4
