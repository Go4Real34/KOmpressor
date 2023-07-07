import os
import subprocess
import platform

from Functions.render_handling import handle_render
from Functions.extra_functions import handle_first_run


def main():
    file_path = os.path.abspath(__file__)
    project_files_folder = file_path.rstrip("console_compressor.py").rstrip("\\")
    kompressor_folder_path = project_files_folder.rstrip("ProjectFiles").rstrip("\\")
    os.chdir(kompressor_folder_path)

    handle_first_run('console')

    handle_render()

    system = platform.system()

    output_path = os.path.join(kompressor_folder_path, "ProjectFiles\\TestIO\\Outputs")

    if system == "Windows":
        subprocess.run(['explorer', output_path])
    elif system == "Linux":
        subprocess.run(['xdg-open', output_path])
    else:
        print("Your operating system is not supported and will be supported if possible in the future.")

    return 0


if __name__ == "__main__":
    main()
