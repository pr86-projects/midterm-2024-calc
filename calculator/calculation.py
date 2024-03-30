from decimal import Decimal
import logging
from typing import Callable
from calculator.operations import add, subtract,multiply, divide

'''Creates an Instance of the Calculation class'''
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Dunder method for object initialization
        self.a = a # property, stores value of a in an instance of this class
        self.b = b # property, stores value of b in an instance of this class
        self.operation = operation # property, stores the operation function

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''This is a factory pattern that returns an instance of this class'''
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
         # Calls stored operation with a and b
        return self.operation(self.a, self.b)

    @property
    def type(self) -> str:
        """Return the type of operation as a string."""
        # Using operation.__name__ to get the function name as the type
        # If the function name does not directly correspond to the desired type string,
        # you might need a mapping or conditional logic here.
        logging.info(f"Operation: {self.operation.__name__}")
        return self.operation.__name__
        
    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        #return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
        return f"Calculation({self.a}, {self.b}, {self.type})"    
