import logging
from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        logging.info("I WIll send something to discord")
        print(f'I WIll send something to discord')

        