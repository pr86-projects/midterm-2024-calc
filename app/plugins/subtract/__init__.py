import logging
from app.commands import Command
from calculator import Calculator
from decimal import Decimal

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            logging.info(f"Subtract number {num2} from {num1}")
        except:
            logging.error(f"Please enter a valid number: {args}")
            print("Please enter a valid number")
            return
        try:
            print(f"The result is: {Calculator.subtract(num1, num2)}")
        except ValueError as e:
            logging.error(f"Error subtracting numbers {num1} and {num2}: {e}") # pragma: no cover
            print(e)
