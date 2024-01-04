import os

from exceptions.IllegalArgumentException import IllegalArgumentException


def handle_help():
    print("Usage: full_unpack [--destination output_dir] archive_file")


def handle_custom_args(args, destination):
    if len(args) < 1:
        raise IllegalArgumentException("No arguments provided", "full_unpack")

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


def path_to_filename(path):
    parts = path.split(os.sep)
    return parts[-1]


def remove_cunp_extension(filename):
    if filename.endswith(".cunp"):
        parts = filename.split(".")
        filename = ".".join(parts[:-1])

    return filename


def create_destination_directory(destination, archive_filename):
    if destination is None:
        destination = remove_cunp_extension(archive_filename)
        if os.path.exists(destination):
            i = 1
            new_destination = f"{destination}_{i}"
            while os.path.exists(new_destination):
                i += 1
                new_destination = f"{destination}_{i}"
            destination = new_destination

    if not os.path.exists(destination):
        os.mkdir(destination)

    return destination


def handle_full_unpack_command(args):
    destination = None
    (args, destination) = handle_custom_args(args, destination)

    args_validation_errors = validate_args(args, destination)
    if len(args_validation_errors) > 0:
        raise IllegalArgumentException("Invalid arguments", "full_unpack", args_validation_errors)

    archive_path = args[0]
    destination = create_destination_directory(destination, path_to_filename(archive_path))
