# Midterm project
This project builds upon the calculator project, with several modifications made to prepare it for the upcoming task:
* If you wish to disable console logging when running the application, remove the "consoleHandler" entry from the "logging.conf" file.
* Upon application startup, the menu command is called after all plugins have been loaded. This ensures the menu is displayed when you run your application. Use the following command: self.command_handler.execute_command('menu').