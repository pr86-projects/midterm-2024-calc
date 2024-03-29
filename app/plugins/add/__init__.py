''' This module contains the AddCommand class which is a subclass of Command class. It implements the execute method to add two numbers. '''
import logging
from app.commands import Command
from calculator import Calculator
from decimal import Decimal

class AddCommand(Command):
    """AddCommand class is a subclass of Command class. It implements the execute method to add two numbers."""
    def execute(self, *args):
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            logging.info(f"Add numbers {num1} and {num2}")
        except:
            logging.error(f"Please enter a valid number: {args}")
            print("Please enter a valid number")
            return
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            print(f"The result is: {Calculator.add(num1, num2)}")
        except ValueError as e:
            logging.error(f"Error adding numbers {num1} and {num2}: {e}") # pragma: no cover
            print(e)
