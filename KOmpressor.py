import os
import sys
import subprocess

from ProjectFiles.Functions.extra_functions import handle_first_run


def main():
    handle_first_run('KOmpressor')

    print("Please select a version.")
    print("[1] - Command Line Tool")
    print("[2] - Web Tool")
    print("[0] - Exit")
    version = input("Enter the number of the version: ")
    while True:
        try:
            version = int(version)
            break
        except ValueError:
            print("Please enter a valid number.")
            exit(0)

    current_directory = os.getcwd()
    python_interpreter = sys.executable
    script_path = os.path.join(current_directory, "ProjectFiles")

    if version == 1:
        script_path = os.path.join(script_path, "console_compressor.py")
    elif version == 2:
        script_path = os.path.join(script_path, "web_compressor.py")
    elif version == 0:
        print("\nExiting...")
        return 0

    subprocess.run([python_interpreter, script_path])

    return 0


if __name__ == '__main__':
    main()
