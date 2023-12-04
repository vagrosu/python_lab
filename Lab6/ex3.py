import os
import sys


def compute_size(dir_path):
    total_size = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            try:
                full_path = os.path.join(root, file)
                total_size += os.path.getsize(full_path)
            except FileNotFoundError:
                print(f"File not found: {full_path}")
            except PermissionError:
                print(f"Permission denied for file: {full_path}")
            except Exception as e:
                print(f"Error accessing file {full_path}: {e}")
    print(f"Total size: {total_size} bytes")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ex3.py <path>")
        print("Example: python ex3.py ./ex3_folder")
    else:
        path = sys.argv[1]
        compute_size(path)
