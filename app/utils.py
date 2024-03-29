from decimal import Decimal
import logging

def process_numbers(args):
    """Process input arguments and return Decimal numbers."""
    try:
        num1 = Decimal(args[0])
        num2 = Decimal(args[1])
        return num1, num2
    except Exception as e:
        logging.error(f"Invalid input {args}: {e}")
        print("Please enter a valid number")
        return None, None