import os.path

from exceptions.IllegalArgumentException import IllegalArgumentException


def validate_paths(paths):
    """
    Checks if each path in the provided list exists, is a file or directory,
    is readable, and if a directory, is not empty. It returns a list of error messages
    for any issues found with the paths.

    Args:
        paths (list(str)): A list of file or directory paths to validate.

    Returns:
        list(str): A list of error messages for any issues found with the paths.
    """
    if len(paths) < 1:
        return ["No paths provided"]

    errors = []
    has_multiple_paths = len(paths) > 1

    for i in range(len(paths)):
        if os.path.exists(paths[i]) is False:
            errors.append(f"Path {paths[i]} does not exist")
            continue

        if has_multiple_paths:
            if os.path.isfile(paths[i]) is False:
                errors.append("For multiple arguments, all must be files")
                continue

        if os.path.isfile(paths[i]):
            if os.access(paths[i], os.R_OK) is False:
                errors.append(f"File {paths[i]} is not readable")
        elif os.path.isdir(paths[i]):
            if os.access(paths[i], os.R_OK) is False:
                errors.append(f"Directory {paths[i]} is not readable")
            else:
                if len(os.listdir(paths[i])) == 0:
                    errors.append(f"Directory {paths[i]} is empty")
                else:
                    for root, folders, files in os.walk(paths[i]):

                        for folder in folders:
                            path = os.path.join(root, folder)
                            if os.access(path, os.R_OK) is False:
                                errors.append(f"Directory {path} is not readable")
                            elif len(os.listdir(str(path))) == 0:
                                errors.append(f"Directory {path} is empty")

                        for file in files:
                            if not file.startswith('.'):
                                path = os.path.join(root, file)
                                if os.access(path, os.R_OK) is False:
                                    errors.append(f"File {path} is not readable")

    return errors


def handle_custom_args(args):
    """
    Processes and validates custom arguments for the 'creare_arhiva' command.

    Args:
        args (list(str)): A list of arguments to process.

    Returns:
        tuple(list(str), str): A tuple containing the modified arguments and the filename, if provided.

    Raises:
        IllegalArgumentException: If the arguments are insufficient.
    """
    if len(args) < 1:
        raise IllegalArgumentException("No arguments provided", "creare_arhiva")

    filename = None
    if args[0] == "--help":
        handle_help()
        exit(0)
    elif args[0] == "--filename":
        if len(args) < 2:
            raise IllegalArgumentException("No filename provided", "creare_arhiva")
        else:
            filename = args[1]
            args = args[2:]

    return args, filename


def handle_help():
    """
    Prints the help message for the 'creare_arhiva' command.

    Returns: None
    """
    print("Usage: creare_arhiva [--filename name] <file/dir path> [<file path> ...]")


def add_extension(filename):
    """
    Adds the '.cunp' extension to the provided filename, if it does not already have it.

    Args:
        filename (str): The filename to add the extension to.

    Returns:
        str: The filename with the '.cunp' extension.
    """
    new_filename = filename
    if not filename.endswith(".cunp"):
        new_filename = f"{filename}.cunp"

    return new_filename


def remove_parent_directory(path):
    """
    Removes the parent directory from the provided path.

    Args:
        path (str): The path to remove the parent directory from.

    Returns:
        str: The path with the parent directory removed.
    """
    parts = path.split(os.sep)
    new_parts = [part for part in parts if part and part != "."][1:]
    return os.sep.join(new_parts)


def create_archive_file(filename):
    """
    Creates an archive file with the provided filename.

    Args:
        filename (str): The filename of the archive file to create.

    Returns:
        file object: The archive file.

    Raises:
        IllegalArgumentException: If the file already exists.
        IOError: If the file cannot be created.
        Exception: If an unexpected error occurs.
    """
    if filename is not None:
        if os.path.exists(add_extension(filename)):
            raise IllegalArgumentException(f"Cannot create archive, file {add_extension(filename)} already exists", "creare_arhiva")
    else:
        filename = "archive"
        if os.path.exists(add_extension(filename)):
            i = 1
            new_filename = f"{filename}_{i}"
            while os.path.exists(add_extension(new_filename)):
                i += 1
                new_filename = f"{filename}_{i}"
            filename = new_filename

    try:
        return open(add_extension(filename), "ab")
    except IOError as e:
        raise IOError(f"Cannot create archive file {add_extension(filename)}: {e.strerror}")
    except Exception as e:
        raise Exception(f"Cannot create archive file {add_extension(filename)}: {e}")


def add_file_to_archive(archive, file_path):
    """
    Adds a file to the archive along with its metadata.

    Args:
        archive (file object): The archive file to add the file to.
        file_path (str): The path of the file to add to the archive.

    Returns: None

    Raises:
        IOError: If the file cannot be read.
        Exception: If an unexpected error occurs.
    """
    try:
        with open(file_path, "rb") as file:
            content = file.read()
        metadata = f"<#METADATA_START#>{remove_parent_directory(file_path)}&{len(content)}<#METADATA_END#>\n"

        archive.write(metadata.encode("utf-8"))
        archive.write(content)
        archive.write(b"\n")
        archive.flush()
        print(f"File {file_path} archived successfully")
    except IOError as e:
        raise IOError(f"Cannot read file {file_path}: {e.strerror}")
    except Exception as e:
        raise Exception(f"Cannot read file {file_path}: {e}")


def write_to_archive_file(archive, file_paths):
    """
    Writes the provided files to the archive.

    Args:
        archive (file object): The archive file to write to.
        file_paths (list(str)): A list of file paths to write to the archive.

    Returns: None
    """
    if os.path.isdir(file_paths[0]):
        for root, folders, files in os.walk(file_paths[0]):
            for file in files:
                if not file.startswith('.'):
                    add_file_to_archive(archive, str(os.path.join(root, file)))
    else:
        for path in file_paths:
            add_file_to_archive(archive, path)
    archive.close()


def handle_creare_arhiva_command(args):
    """
    Processes the command arguments, validates them, and then proceeds
    to create an archive file with the provided name and containing the provided files.

    Args:
        args (list(str)): A list of arguments for the 'creare_arhiva' command.

    Returns: None

    Raises:
        IllegalArgumentException: If the arguments are invalid or insufficient.
    """
    (paths, filename) = handle_custom_args(args)

    args_validation_errors = validate_paths(paths)
    if len(args_validation_errors) > 0:
        raise IllegalArgumentException("Invalid arguments", "creare_arhiva", args_validation_errors)

    if len(paths) > 0:
        archive = create_archive_file(filename)
        write_to_archive_file(archive, paths)

        print(f"Archive {archive.name} created successfully")
