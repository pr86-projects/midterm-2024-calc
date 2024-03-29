import logging
from app.commands import Command
from calculator import Calculator
from decimal import Decimal

class DivideCommand(Command):
    def execute(self, *args):
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            logging.info(f"Divide number {num1} by {num2}")
        except:
            print("Please enter a valid number")
            logging.error(f"Please enter a valid number: {args}")
            return
        try:
            print(f"The result is: {Calculator.divide(num1, num2)}")
        except ValueError as e:
            print(e)
            logging.error(f"Error dividing numbers {num1} and {num2}: {e}") # pragma: no cover
