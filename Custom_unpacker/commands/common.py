"""Common functions for commands."""

import os


def get_archive_files(archive_path):
    """
    Reads a '.cunp' archive file, parses its contents
    to extract metadata, and returns a list of file names included
    in the archive.

    Args:
        archive_path (str): The path to the archive file.

    Returns:
        list(str): A list of file names included in the archive.

    Raises:
        Exception: If the archive file cannot be read.
    """
    try:
        files = []
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
                files.append(metadata.split("&")[0])
                index = end_index + len(end_delimiter)

        return files
    except Exception as e:
        raise Exception(f"Cannot read archive file {archive_path}: {e}")


def path_to_filename(path):
    """
    Extracts the file name from a path.

    Args:
        path (str): The path to extract the file name from.

    Returns:
        str: The extracted file name.
    """
    parts = path.split(os.sep)
    return parts[-1]


def remove_cunp_extension(filename):
    """
    Removes the '.cunp' extension from a file name, if present.

    Args:
        filename (str): The file name to remove the extension from.

    Returns:
        str: The filename with the '.cunp' extension removed, if it was present.
    """
    if filename.endswith(".cunp"):
        parts = filename.split(".")
        filename = ".".join(parts[:-1])

    return filename


def create_destination_dir(destination, archive_filename):
    """
    Creates a destination directory for unpacking an archive.

    If a destination path is not provided, it creates a new directory with a name
    based on the archive file name. If the directory already exists, it appends an
    incrementing number to create a unique directory.

    Args:
        destination (str): The desired path for the destination directory. If None,
                           a directory is created based on 'archive_filename'.
        archive_filename (str): The name of the archive file, used to generate
                                a directory name if 'destination' is None.

    Returns:
        str: The path to the created destination directory.
    """
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
