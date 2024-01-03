import os

from exceptions.IllegalArgumentException import IllegalArgumentException


def handle_help():
    print("Usage: listare_continut archive_file")


def handle_custom_args(args):
    if len(args) < 1:
        raise IllegalArgumentException("No arguments provided", "listare_continut")

    if args[0] == "--help":
        handle_help()
        exit(0)


def validate_args(file_path):
    if len(file_path) < 1:
        raise IllegalArgumentException("Invalid number of arguments", "listare_continut")

    if not os.path.exists(file_path):
        raise IllegalArgumentException(f"File {file_path} does not exist", "listare_continut")

    if not file_path.endswith(".cunp"):
        raise IllegalArgumentException(f"File {file_path} is not a .cunp file", "listare_continut")

    if not os.path.isfile(file_path):
        raise IllegalArgumentException(f"Argument must be a file", "listare_continut")
    elif os.access(file_path, os.R_OK) is False:
        raise IllegalArgumentException(f"File {file_path} is not readable", "listare_continut")


def get_archive_files(archive_path):
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


def print_archive_files(archive_path, archive_files):
    if len(archive_files) == 0:
        raise Exception(f"Archive {archive_path} is empty")

    print(f"Archive {archive_path} files:")
    for file in archive_files:
        print(f" -> {file}")


def handle_listare_continut_command(args):
    handle_custom_args(args)
    validate_args(args[0])

    archive_files = get_archive_files(args[0])
    print_archive_files(args[0], archive_files)
