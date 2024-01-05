import os

from commands.common import get_archive_files, create_destination_dir, path_to_filename
from exceptions.IllegalArgumentException import IllegalArgumentException


def handle_help():
    """
    Prints the help message for the 'unpack' command.

    Returns: None
    """
    print("Usage: unpack --archive <archive path> [--destination <output dir>] <file name> [<file name> ...]")


def handle_custom_args(args):
    """
    Processes and validates custom arguments for the 'unpack' command.

    Args:
        args (list(str)): The list of arguments to process.

    Returns:
        tuple(list(str), str, str): A tuple containing the remaining arguments, the archive path and the destination
        directory, if provided.

    Raises:
        IllegalArgumentException: If the arguments are insufficient.
    """
    if len(args) < 1:
        raise IllegalArgumentException("No arguments provided", "unpack")

    if args[0] == "--help":
        handle_help()
        exit(0)
    elif args[0] == "--archive":
        if len(args) < 2:
            raise IllegalArgumentException("No archive file provided", "unpack")
        else:
            archive_path = args[1]
            args = args[2:]
    else:
        raise IllegalArgumentException("No archive file provided", "unpack")

    destination = None
    if len(args) > 0:
        if args[0] == "--destination":
            if len(args) < 2:
                raise IllegalArgumentException("No destination directory provided", "unpack")
            else:
                destination = args[1]
                args = args[2:]

    return args, archive_path, destination


def validate_args(args, archive_files, destination):
    """
    Checks if each argument is a valid file name in the archive and
    if the destination directory is valid.

    Args:
        args (list(str)): The list of arguments to validate.
        archive_files (list(str)): The list of files in the archive.
        destination (str): The destination directory to validate.

    Returns:
        list(str): A list of errors encountered during validation.
    """
    errors = []
    if len(args) < 1:
        errors.append("No file names provided")

    if destination is not None:
        if os.path.exists(destination):
            errors.append(f"Destination directory {destination} already exists")

    for arg in args:
        if arg not in archive_files:
            errors.append(f"File {arg} does not exist in archive")

    return errors


def unarchive_file(archive_path, destination, files_to_unarchive):
    """
    Unpacks the specified contents of the archive file into the destination directory.

    Args:
        archive_path (str): The path to the archive file.
        destination (str): The destination directory to unpack the contents of the archive.
        files_to_unarchive (list(str)): The list of files to unpack from the archive.

    Returns: None

    Raises:
        Exception: If an error occurs while unarchiving the file.
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
                file_name = metadata_parts[0]
                file_size = int(metadata_parts[1])
                # remove newline
                end_index += 1

                if file_name in files_to_unarchive:
                    file_content = content[end_index + len(end_delimiter):end_index + len(end_delimiter) + file_size]
                    file_path = os.path.join(destination, file_name)

                    if not os.path.exists(os.path.dirname(file_path)):
                        os.makedirs(os.path.dirname(file_path))

                    with open(file_path, "wb") as file:
                        file.write(file_content)
                        print(f"File {file_name} unarchived successfully")

                index = end_index + len(end_delimiter) + file_size
    except Exception as e:
        raise Exception(f"Error while unarchiving file {archive_path}: {e}")


def handle_unpack_command(args):
    """
    Processes the command arguments, validates them, and then proceeds
    to unpack the specified contents of the specified archive into the destination directory.

    Args:
        args (list(str)): A list of arguments for the 'unpack' command.

    Returns: None

    Raises:
        IllegalArgumentException: If the arguments are invalid or insufficient.
    """
    (files_to_unarchive, archive_path, destination) = handle_custom_args(args)
    archive_files = get_archive_files(archive_path)
    args_validation_errors = validate_args(files_to_unarchive, archive_files, destination)
    if len(args_validation_errors) > 0:
        raise IllegalArgumentException("Invalid arguments", "unpack", args_validation_errors)

    destination = create_destination_dir(destination, path_to_filename(archive_path))
    unarchive_file(archive_path, destination, files_to_unarchive)

    print(f"Archive {archive_path} unarchived successfully")
