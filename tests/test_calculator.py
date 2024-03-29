'''Testing the calculator class'''
from calculator import Calculator

def test_calculator_add():
    '''Testing the static Calculator add function'''
    assert Calculator.add(2,2) == 4

def test_calculator_subtract():
    '''Testing the static Calculator subtract function'''
    assert Calculator.subtract(10,7) == 3

def test_calculator_multiply():
    '''Testing the static Calculator multiply function'''
    assert Calculator.multiply(3,4) == 12

def test_calculator_divide():
    '''Testing the static Calculator divide function'''
    assert Calculator.divide(10,2) == 5
