import sys
import logging
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        #print(f'Menu')
        commands = ['add number1 number2        Add two numbers', 
                    'subtract number1 number2   Subtract two numbers', 
                    'multiply number1 number2   Multiply two numbers', 
                    'divide number1 number2     Divide two numbers', 
                    'greet                      Greet the user',   
                    'goodbye                    Say goodbye to the user', 
                    'discord                    Send something to Discord', 
                    'exit                       Exits the app']  # Replace with the actual list of commands
        logging.info("Available commands:")
        print('Available commands:')
        for command in commands:
            print(f'- {command}')
        