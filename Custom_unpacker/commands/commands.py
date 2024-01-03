from commands.creare_arhiva import handle_creare_arhiva_command
from commands.listare_continut import handle_listare_continut_command
from commands.full_unpack import handle_full_unpack_command
from commands.unpack import handle_unpack_command
from exceptions.InvalidCommandException import InvalidCommandException


def handle_help_command(*args):
    print("Available commands:")
    print(" -> creare_arhiva")
    print(" -> listare_continut")
    print(" -> full_unpack")
    print(" -> unpack")
    print(" -> --help")


def handle_command(command, args):
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
