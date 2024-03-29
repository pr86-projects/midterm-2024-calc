import sys
from app.commands import Command


class ExitCommand(Command): # pragma: no cover
    def execute(self):
        # Do not use sys.exit() as the App class handles the exit process
        #sys.exit("Exiting...")
        pass
        