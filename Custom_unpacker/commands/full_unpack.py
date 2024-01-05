import os

from commands.common import path_to_filename, create_destination_dir
from exceptions.IllegalArgumentException import IllegalArgumentException


def handle_help():
    """
    Prints the help message for the 'full_unpack' command.

    Returns: None
    """
    print("Usage: full_unpack [--destination <output dir>] <archive path>")


def handle_custom_args(args):
    """
    Processes and validates custom arguments for the 'full_unpack' command.

    Args:
        args (list(str)): The list of arguments to process.

    Returns:
         tuple(list(str), str): A tuple containing the remaining arguments and the destination directory, if provided.

    Raises:
        IllegalArgumentException: If the arguments are insufficient.
    """
    if len(args) < 1:
        raise IllegalArgumentException("No arguments provided", "full_unpack")

    destination = None
    if args[0] == "--help":
        handle_help()
        exit(0)
    elif args[0] == "--destination":
        if len(args) < 2:
            raise IllegalArgumentException("No destination directory provided", "full_unpack")
        else:
            destination = args[1]
            args = args[2:]

    return args, destination


def validate_args(args, destination):
    """
    Validates the arguments provided for the 'full_unpack' command.

    Args:
        args (list(str)): The list of arguments to validate.
        destination (str): The destination directory to validate.

    Returns:
        list(str): A list of errors encountered during validation.
    """
    errors = []

    if destination is not None:
        if os.path.exists(destination):
            errors.append(f"Destination directory {destination} already exists")

    if len(args) < 1:
        errors.append("No archive file provided")
    else:
        archive_path = args[0]
        if not os.path.exists(archive_path):
            errors.append(f"File {archive_path} does not exist")
        elif not archive_path.endswith(".cunp"):
            errors.append(f"File {archive_path} is not a .cunp file")
        elif not os.path.isfile(archive_path):
            errors.append(f"Argument must be a file")
        elif os.access(archive_path, os.R_OK) is False:
            errors.append(f"Archive {archive_path} is not readable")

    return errors


def unarchive_file(archive_path, destination):
    """
    Unpacks the contents of the archive file into the specified destination directory.


    Args:
        archive_path (str): The path to the archive file.
        destination (str): The destination directory to unpack the contents of the archive.

    Returns: None

    Raises:
        Exception: If an error occurs while unpacking the archive.
    """
    try:
        with open(archive_path, "rb") as archive:
            content = archive.read()

            start_delimiter = b'<#METADATA_START#>'
            end_delimiter = b'<#METADATA_END#>'

            index = 0

            while True:
                start_index = content.find(start_delimiter, index)
                if start_index == -1:
                    break
                end_index = content.find(end_delimiter, start_index)
                if end_index == -1:
                    break

                metadata = content[start_index + len(start_delimiter):end_index].decode("utf-8")
                metadata_parts = metadata.split("&")
                file_path = metadata_parts[0]
                file_size = int(metadata_parts[1])
                # remove newline
                end_index += 1

                file_content = content[end_index + len(end_delimiter):end_index + len(end_delimiter) + file_size]
                file_path = os.path.join(destination, file_path)

                if not os.path.exists(os.path.dirname(file_path)):
                    os.makedirs(os.path.dirname(file_path))

                with open(file_path, "wb") as file:
                    file.write(file_content)
                    print(f"File {file_path} unarchived successfully")

                index = end_index + len(end_delimiter) + file_size
    except Exception as e:
        raise Exception(f"Error while unarchiving file {archive_path}: {e}")


def handle_full_unpack_command(args):
    """
    Processes the command arguments, validates them, and then proceeds
    to unpack the contents of the specified archive into the destination directory.

    Args:
        args (list(str)): A list of arguments for the 'full_unpack' command.

    Returns: None

    Raises:
        IllegalArgumentException: If the arguments are insufficient or invalid.
    """
    (args, destination) = handle_custom_args(args)

    args_validation_errors = validate_args(args, destination)
    if len(args_validation_errors) > 0:
        raise IllegalArgumentException("Invalid arguments", "full_unpack", args_validation_errors)

    archive_path = args[0]
    destination = create_destination_dir(destination, path_to_filename(archive_path))
    unarchive_file(archive_path, destination)

    print(f"Archive {archive_path} unarchived successfully")
