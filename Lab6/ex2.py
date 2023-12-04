import os
import sys


def rename_files(dir_path):
    if os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        files.sort()
        for i, full_file_name in enumerate(files):
            full_path = os.path.join(dir_path, full_file_name)
            file_name, file_extension = os.path.splitext(full_file_name)[0], os.path.splitext(full_file_name)[1]
            new_file_name = f"{file_name}{i + 1}{file_extension}"
            new_full_path = os.path.join(dir_path, new_file_name)
            try:
                os.rename(full_path, new_full_path)
            except FileNotFoundError:
                print(f"File not found: {full_path}")
            except PermissionError:
                print(f"Permission denied for file: {full_path}")
            except Exception as e:
                print(f"Error renaming file {full_path}: {e}")
    else:
        print("Invalid path")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ex2.py <path>")
        print("Example: python ex2.py ./ex2_folder")
    else:
        path = sys.argv[1]
        rename_files(path)