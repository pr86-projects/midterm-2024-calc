# Midterm project
This project builds upon the calculator project, with several modifications made to prepare it for the upcoming task:
* If you wish to disable console logging when running the application, remove the "consoleHandler" entry from the "logging.conf" file.
* Upon application startup, the menu command is called after all plugins have been loaded. This ensures the menu is displayed when you run your application. Use the following command: self.command_handler.execute_command('menu').


- Removed multi processing so the history is available in the main process
- To remove logging on the console when you run the application, remove "consoleHandler" from "logging.conf" file
- On application start call the menu command after loading all the pluggins. This will show the menu when you run your application.
    self.command_handler.execute_command('menu')
- Added CsvCommand class that acceps commands (save, print, remove)
- Max canculation history can be configured using the environment variable
- Folder and finames are configured in the environment variables
- Absolute path is used to refer to the csv file 
