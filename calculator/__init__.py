from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
from typing import Callable

'''Class with static methods. No instance is created.'''
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation) # add instance of this class/operation to the history
        return calculation.perform()
    
    @staticmethod
    def add(a: Decimal,b: Decimal) -> Decimal:
        # This is a static method that pass the add function from calculator.operations
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal,b: Decimal) -> Decimal:
        # This is a static method that pass the subtract function from calculator.operations
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply (a: Decimal,b: Decimal) -> Decimal:
        # This is a static method that pass the multiply function from calculator.operations
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal,b: Decimal) -> Decimal:
        # This is a static method that pass the divide function from calculator.operations
        return Calculator._perform_operation(a, b, divide)
