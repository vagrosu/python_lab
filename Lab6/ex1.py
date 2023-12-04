import os.path
import sys


def read_files(path, extension):
    global file
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(extension):
                    full_path = os.path.join(root, file_name)
                    try:
                        file = open(full_path, mode='r')
                        print(f"Contents of {file_name}:")
                        print(file.read())
                        print("\n")
                    except FileNotFoundError:
                        print(f"File not found: {full_path}")
                    except PermissionError:
                        print(f"Permission denied for file: {full_path}")
                    except Exception as e:
                        print(f"Error opening file {full_path}: {e}")
                    finally:
                        file.close()
    else:
        print("Invalid path")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python ex1.py <path> <extension>")
        print("Example: python ex1.py ./ex1_folder .txt")
    else:
        dir_path, file_extension = sys.argv[1], sys.argv[2]
        read_files(dir_path, file_extension)
