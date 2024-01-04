import os

from commands.common import path_to_filename, create_destination_dir
from exceptions.IllegalArgumentException import IllegalArgumentException


def handle_help():
    print("Usage: full_unpack [--destination <output dir>] <archive path>")


def handle_custom_args(args):
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
    (args, destination) = handle_custom_args(args)

    args_validation_errors = validate_args(args, destination)
    if len(args_validation_errors) > 0:
        raise IllegalArgumentException("Invalid arguments", "full_unpack", args_validation_errors)

    archive_path = args[0]
    destination = create_destination_dir(destination, path_to_filename(archive_path))
    unarchive_file(archive_path, destination)

    print(f"Archive {archive_path} unarchived successfully")