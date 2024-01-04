import os


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


def path_to_filename(path):
    parts = path.split(os.sep)
    return parts[-1]


def remove_cunp_extension(filename):
    if filename.endswith(".cunp"):
        parts = filename.split(".")
        filename = ".".join(parts[:-1])

    return filename


def create_destination_dir(destination, archive_filename):
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
