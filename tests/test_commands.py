"""
This module contains tests for the all Commands.
"""
#import pytest
import sys
from app import App
from app.plugins.discord import DiscordCommand
from app.plugins.email import EmailCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.menu import MenuCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.commands import Command, CommandHandler

def test_greet_command(capfd):
    """This test verifies that the GreetCommand class prints 'Hello, World!' when executed."""
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """This test verifies that the GoodbyeCommand class prints 'Goodbye' when executed. """
    command = GoodbyeCommand()
    command.execute()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "Goodbye\n", "The GreetCommand should print 'Hello, World!'"

def test_add_command(capfd):
    """This test verifies that the AddCommand class prints 'The result is: 10' when executed."""
    command = AddCommand()
    command.execute(2, 8)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: 10\n", "The AddCommand should print 'The result is: 10'"

def test_add_command_invalid_input(capfd):
    """This test verifies that the AddCommand class prints 'Please enter a valid number' when executed with invalid input."""
    command = AddCommand()
    command.execute("two", "three")
    captured = capfd.readouterr()
    assert "Please enter a valid number" in captured.out

def test_add_command_boundary_values(capfd):
    """This test verifies that the AddCommand class prints 'The result is: 18446744073709551614' when executed with sys.maxsize."""
    command = AddCommand()
    command.execute(str(sys.maxsize), str(sys.maxsize))
    out, err = capfd.readouterr()  # pylint: disable=unused-variable
    # Assuming Calculator.add can handle large numbers and doesn't overflow
    expected_sum = sys.maxsize + sys.maxsize
    assert f"The result is: {expected_sum}" in out

def test_subtract_command(capfd):
    """This test verifies that the SubtractCommand class prints 'The result is: -6' when executed."""
    command = SubtractCommand()
    command.execute(2, 8)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: -6\n", "The SubtractCommand should print 'The result is: -6'"

def test_subtract_command_invalid_input(capfd):
    """This test verifies that the SubtractCommand class prints 'Please enter a valid number' when executed with invalid input."""
    command = SubtractCommand()
    command.execute("two", "three")
    captured = capfd.readouterr()
    assert "Please enter a valid number" in captured.out

def test_multiply_command(capfd):
    """This test verifies that the MultiplyCommand class prints 'The result is: 16' when executed."""
    command = MultiplyCommand()
    command.execute(2, 8)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: 16\n", "The MultiplyCommand should print 'The result is: 16'"

def test_multiply_command_invalid_input(capfd):
    """This test verifies that the MultiplyCommand class prints 'Please enter a valid number' when executed with invalid input."""
    command = MultiplyCommand()
    command.execute("two", "three")
    captured = capfd.readouterr()
    assert "Please enter a valid number" in captured.out

def test_divide_command(capfd):
    """This test verifies that the DivideCommand class prints 'The result is: 4' when executed."""
    command = DivideCommand()
    command.execute(8, 2)
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "The result is: 4\n", "The DivideCommand should print 'The result is: 4'"

def test_divide_command_invalid_input(capfd):
    """This test verifies that the DivideCommand class prints 'Please enter a valid number' when executed with invalid input."""
    command = DivideCommand()
    command.execute("two", "three")
    captured = capfd.readouterr()
    assert "Please enter a valid number" in captured.out

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    #with pytest.raises(SystemExit) as e:
    #    app.start()  # Assuming App.start() is now a static method based on previous discussions
    app.start()
    captured = capfd.readouterr()
    #assert str(e.value) == "Hello, World!", "The app did not exit as expected"
    assert "Hello, World!" in captured.out
    assert "Exiting application..." in captured.out

def test_discord_command(capfd):
    """This test verifies that the DiscordCommand class prints 'I WIll send something to discord' when executed. """
    command = DiscordCommand()
    command.execute()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "I WIll send something to discord\n", "The DiscordCommand should print 'I WIll send something to discord'"

def test_email_command(capfd):
    """This test verifies that the EmailCommand class prints 'I will email you. """
    command = EmailCommand()
    command.execute()
    out, err = capfd.readouterr() # pylint: disable=unused-variable
    assert out == "I will email you.\n", "The DiscordCommand should print 'I will email you.'"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    #with pytest.raises(SystemExit) as e:
    #    app.start()  # Assuming App.start() is now a static method based on previous discussions
    app.start()
    captured = capfd.readouterr()
    #assert str(e.value) == "Exiting...", "The app did not exit as expected"
    assert "Exiting application..." in captured.out

def test_menu_command_output(capfd):
    """Test that MenuCommand prints the list of available commands."""
    command = MenuCommand()
    command.execute()
    captured = capfd.readouterr()
    expected_commands = [
        'add number1 number2        Add two numbers', 
        'subtract number1 number2   Subtract two numbers', 
        'multiply number1 number2   Multiply two numbers', 
        'divide number1 number2     Divide two numbers', 
        'greet                      Greet the user',   
        'goodbye                    Say goodbye to the user', 
        'discord                    Send something to Discord', 
        'exit                       Exits the app'
    ]
    for expected_command in expected_commands:
        assert f'- {expected_command}' in captured.out
    assert 'Available commands:' in captured.out

# Create a mock command to use for testing
class MockCommand(Command):
    """ A mock command that always returns the same output when executed."""
    def execute(self, *args):
        print( "Mock command executed")

def test_register_command():
    """Test registering a command with the command handler."""
    command_handler = CommandHandler()
    mock_command = MockCommand()
    command_handler.register_command("mock", mock_command)
    assert "mock" in command_handler.commands

def test_execute_registered_command(capfd):
    """Test executing a command that has been registered with the command handler."""
    command_handler = CommandHandler()
    mock_command = MockCommand()
    command_handler.register_command("mock", mock_command)
    command_handler.execute_command("mock")
    captured = capfd.readouterr()
    assert "Mock command executed" in captured.out

def test_execute_unregistered_command(capfd):
    """Test attempting to execute a command that hasn't been registered."""
    command_handler = CommandHandler()
    command_handler.execute_command("unregistered")
    captured = capfd.readouterr()
    assert "No such command: unregistered" in captured.out
