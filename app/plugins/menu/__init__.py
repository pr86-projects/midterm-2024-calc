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
                    'exit                       Exits the app']  # Replace with the actual list of commands
        logging.info("Follwing commands are available:")
        logging.info('\n'.join(commands))
        print('Follwing commands are available:')
        for command in commands:
            print(f'- {command}')
        