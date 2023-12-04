import os
import sys


def get_extensions(dir_path):
    extensions = {}
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            try:
                full_path = os.path.join(root, file)
                extension = os.path.splitext(full_path)[1]
                if extension in extensions:
                    extensions[extension] += 1
                else:
                    extensions[extension] = 1
            except FileNotFoundError:
                print(f"File not found: {full_path}")
            except PermissionError:
                print(f"Permission denied for file: {full_path}")
            except Exception as e:
                print(f"Error accessing file {full_path}: {e}")
    return extensions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ex4.py <path>")
        print("Example: python ex4.py ./ex3_folder")
    else:
        path = sys.argv[1]
        print(get_extensions(path))