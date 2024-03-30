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
- Modify the yml file to generate env file during GitHub workflow


### Command Design Pattern: 
The Command design pattern was used to encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. In this project, this pattern is implemented through the Command and CommandHandler classes. Commands encapsulate all the information needed to perform an action or trigger an event.
Code Implementation: All classes under the plugin folder that are inheriting from an abstract Command class. Following are the commands used
- add
- subtract
- multiply
- divide
- *csv sub commands*
- csv print : 
 Example: 
    1: Calculation(2, 4, add)
    2: Calculation(4, 1, subtract)
    3: Calculation(3, 5, multiply)
    4: Calculation(4, 2, divide)
    5: Calculation(5, 6, add)
    6: Calculation(1, 1, add)
    7: Calculation(2, 2, add)
- csv save
- csv remove

### Usage of Environment Variables
Environment variables are used to manage configuration settings outside of the application's codebase, making the application more adaptable to different environments without code changes.
Code Implementation: Environment variables are loaded using load_dotenv() in the App class's constructor, and accessed throughout the application using the get_environment_variable method.
Following settings are stored in the environment variables
- CALC_HISTORY_PATH : name of the folder for storing csv file
- FILE_NAME: name of the file
- MAX_HISTORY: maximum number of calculations that can be stored in the csv file
  
### Logging
Logging is used to record significant events and errors that occur during the execution of the application. It's essential for debugging and monitoring the application's behavior.
Code Implementation: The configure_logging method in the App class sets up logging based on a configuration file or defaults to basic configuration if the file is not found. See the implementation here.

### Exception Handling Strategies
#### Look Before You Leap (LBYL): 
This approach involves checking conditions before making an operation to avoid exceptions. It's characterized by explicit checks before operations. 
Code Implementation: An example is checking if a file exists before trying to open it. See an example here.
    def load_from_csv(self): the code in this method check if the csv file for storing history exists before calling the reader method
#### Easier to Ask for Forgiveness than Permission (EAFP): 
This approach is characterized by trying to perform the operation and catching exceptions if they occur. It is more Pythonic and often leads to cleaner code.
Code Implementation: An example is attempting to remove calculation from Calculation history in the CsvCommand class that catches index out of bounds error.