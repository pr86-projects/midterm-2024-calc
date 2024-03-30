import csv
from decimal import Decimal
import decimal
import os
import logging
from dotenv import load_dotenv
import pandas as pd
#from app import App
from app.commands import Command
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract,multiply, divide
#from dotenv import load_dotenv

class CsvCommand(Command):
    settings = {}
    max_history=5
    def __init__(self):
        #def __init__(self, data_dir, history_file_name):
        # Load file settings from environment variables
        load_dotenv()
        self.load_environment_variables()
        #self.data_dir = App.get_environment_variable('CALC_HISTORY_PATH')
        #self.history_file_name = App.get_environment_variable('FILE_NAME')
        self.data_dir = self.get_environment_variable('CALC_HISTORY_PATH', 'data')
        logging.info(f"Data directory: {self.data_dir}")

        self.history_file_name = self.get_environment_variable('FILE_NAME', 'calculator_history.csv')
        self.history_file_path = os.path.join(self.data_dir, self.history_file_name)
        self.max_history = int(self.get_environment_variable('MAX_HISTORY','5'))
        logging.info(f"File name: {self.history_file_name}")
        logging.info(f"File Path: {self.history_file_path}")
        # Check if the data directory exists and is writable
        self.ensure_directory(self.data_dir)
        self.absolute_path = os.path.abspath(self.history_file_path)
        logging.info(f"Absolute Path: {self.absolute_path}")

    def ensure_directory(self, data_dir):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"{data_dir} directory '{self.data_dir}' created.")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            raise PermissionError(f"The directory '{data_dir}' is not writable.")
    
    def load_environment_variables(self):
        """Load environment variables from .env file."""
        #settings = {key: value for key, value in os.environ.items()}
        CsvCommand.settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")

    @staticmethod
    def get_environment_variable(env_var: str, default=None):
        """Get the value of the environment variable."""
        return CsvCommand.settings.get(env_var, None)

    def print_sub_commands(self):
        """Prints the available sub-commands for the CsvCommand."""
        sub_commands = [
            'save - Saves the current calculations history to a CSV file.',
            #'load - Loads calculations history from a CSV file.',
            'print - Prints the current calculations history.',
            'remove <index> - Removes a calculation from history at the specified index.'
        ]
        print("Available sub-commands for Csv file I/O:")
        for sub_command in sub_commands:
            print(f"  {sub_command}")

    def execute(self, *args):
        logging.info("Inside CsvCommand execute method")
        
        if not args:
            logging.error("No sub-command provided to CsvCommand.")
            print("Available sub-commands: save, load, print, add, remove")
            self.print_sub_commands()  # Call the method to print sub-commands when none is provided
            return

        sub_command = args[0].lower()
        if sub_command == 'save':
            self.save_to_csv()
        #elif sub_command == 'load':
        #    self.load_from_csv()
        elif sub_command == 'print':
            self.print_calculations()
        elif sub_command == 'remove':
            self.remove_calculation(*args[1:])
        else:
            logging.error(f"Unknown sub-command: {sub_command}")
            print("Available sub-commands: save, print, remove")
        

    def save_to_csv(self):
        if len(Calculations.get_history()) > self.max_history:
            print(f"Calculations history cannot be greater than {self.max_history}. Please remove few calculations and try again.")
            return
        logging.info(f"Saving calculations history to CSV.") 
        # Convert Calculations history to DataFrame and save to CSV
        df = pd.DataFrame([{
            'a': calc.a,
            'b': calc.b,
            'operation': calc.type  # Use the type property
        } for calc in Calculations.get_history()])
        df.to_csv(self.absolute_path, index=False)
        print('Calculations history saved to CSV file.')
        logging.info(f"Calculations history saved to {self.history_file_path}.")

    def load_from_csv(self):
        # Check if the file exists before trying to open it
        if not os.path.exists(self.history_file_path):
            logging.info(f"No existing history at {self.history_file_path}. Skipping load.")
            return
    
        # Load calculations from CSV and recreate Calculation objects
        logging.info(f"Loading calculations history.")
        operation_mapping = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        
        with open(self.history_file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                logging.debug(f"Processing row: {row}")
                if len(row) < 3:  # Ensure the row has enough data
                    continue
                #a, b, operation_name = Decimal(row[0]), Decimal(row[1]), row[2]
                try:
                    a, b = Decimal(row[0]), Decimal(row[1])
                except decimal.InvalidOperation:
                    logging.error(f"Invalid operands in row: {row}. Skipping.")
                    continue  # Skip this row and go to the next one

                operation_name = row[2]
                operation = operation_mapping.get(operation_name)
                if operation is None:
                    continue  # Skip unknown operations

                calculation = Calculation.create(a, b, operation)
                Calculations.add_calculation(calculation)

    def print_calculations(self):
        logging.info("Printing calculations history.")
        history = Calculations.get_history()
        if not history:
            print("No calculations in history.")
            return
        #for calc in history:
        #    print(f"{calc.a} {calc.operation.__name__} {calc.b} = {calc.result}")
        for idx, calculation in enumerate(Calculations.get_history(), start=1):
            print(f"{idx}: {calculation}")    

    def remove_calculation(self, item):
        logging.info(f"Attempting to delete calculation at index: {item}")
        try:
            idx = int(item) - 1  # Convert to 0-based index
        except ValueError:
            logging.error(f"Invalid index provided: {item}. Index must be a number.")
            print(f"Invalid index: {item}. Please provide a valid numeric index.")
            return

        try:
            Calculations.remove_calculation_by_index(idx)
            logging.info(f"Calculation at index {idx + 1} successfully removed.")
            print(f"Calculation at index {idx + 1} successfully removed.")
        except IndexError:
            logging.error(f"Index out of range: {idx + 1}.")
            print(f"Index out of range: {idx + 1}. Please provide an index within the history range.")
