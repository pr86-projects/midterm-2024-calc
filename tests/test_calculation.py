"""
This module contains tests for the calculator operations and Calculation class.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide # pylint: disable=unused-import

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both integer and decimal operands to ensure the operations work correctly under different conditions.
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    Parameters:
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (function): The operation to perform.
        expected (Decimal): The expected result.
    """
    calc = Calculation.create(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the string representation of the Calculation class.
    """
    calc = Calculation.create(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation.create(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
