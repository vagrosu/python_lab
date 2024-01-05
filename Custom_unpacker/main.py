"""
This is the main file of the project.

It handles command-line arguments passed to the application and
calls a master handler function to handle the commands. If an invalid command
is provided, or if an error occurs, it prints an error message and exits.
"""

import sys

from commands.commands import handle_command, handle_help_command
from exceptions.IllegalArgumentException import IllegalArgumentException
from exceptions.InvalidCommandException import InvalidCommandException

if __name__ == "__main__":
    """
    The main entry point of the application.
    
    This block processes command-line arguments, executes the relevant command handler,
    and handles various exceptions that might occur during command processing.
    
    Returns: None
    
    Exceptions:
        - IllegalArgumentException: raised when an invalid argument is provided.
        - InvalidCommandException: raised when an invalid command is provided.
        - Exception: raised when an unexpected error occurs.    
    """
    commands = sys.argv[1:]

    try:
        if len(commands) > 0:
            handle_command(commands[0], commands[1:])
        else:
            raise InvalidCommandException("No command provided")

    except IllegalArgumentException as e:
        print("Error: " + e.message)
        for error in e.errors:
            print(" -> " + error)

    except InvalidCommandException as e:
        print("Error: " + e.message)
        handle_help_command()

    except Exception as e:
        print("Error: " + str(e))
