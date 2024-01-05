from commands.creare_arhiva import handle_creare_arhiva_command
from commands.listare_continut import handle_listare_continut_command
from commands.full_unpack import handle_full_unpack_command
from commands.unpack import handle_unpack_command
from exceptions.InvalidCommandException import InvalidCommandException


def handle_help_command(*args):
    """
    Prints a list of available commands

    Args:
        *args(any): Arbitrary argument list, not used in this function.

    Returns: None
    """
    print("Available commands:")
    print(" -> creare_arhiva")
    print(" -> listare_continut")
    print(" -> full_unpack")
    print(" -> unpack")
    print(" -> --help")


def handle_command(command, args):
    """
    Maps a command name to its respective handler function and executes it.

    Args:
        command (str): The name of the command to be executed.
        args (list): A list of arguments to be passed to the command handler function.

    Raises:
        InvalidCommandException: If the command is not found in the available commands.

    Returns: None
    """
    available_commands = {
        "creare_arhiva": handle_creare_arhiva_command,
        "listare_continut": handle_listare_continut_command,
        "full_unpack": handle_full_unpack_command,
        "unpack": handle_unpack_command,
        "--help": handle_help_command
    }

    if command not in available_commands:
        raise InvalidCommandException(f"Invalid command {command}")

    available_commands[command](args)
