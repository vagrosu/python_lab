import sys

from commands.commands import handle_command, handle_help_command
from exceptions.IllegalArgumentException import IllegalArgumentException
from exceptions.InvalidCommandException import InvalidCommandException

if __name__ == "__main__":
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
