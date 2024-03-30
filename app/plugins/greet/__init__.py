import logging
from app.commands import Command
from icecream import ic
from app import App

class GreetCommand(Command):
    def execute(self):
        logging.info("Hello, World!")
        logging.debug(ic(App))
        print("Hello, World!")
        