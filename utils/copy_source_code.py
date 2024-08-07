import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
file_name = os.path.join(base_dir, "source_code.txt")


def write_file_source_code(file_path):
    # Read and write the source code of the file to a file
    with open(file_path, "r") as f:
        with open(file_name, "a") as file:
            file.write(f.read())
            file.write("\n\n")


def write_source_code_inside_folder(folder_path):
    # Read and write all the source codes of the folder to a file

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                write_file_source_code(file_path)

        for dir_name in dirs:
            if dir_name in ["__pycache__", ".idea", "venv", "env"]:
                continue

            dir_path = os.path.join(root, dir_name)
            write_source_code_inside_folder(dir_path)


if __name__ == "__main__":
    # # uncomment the following lines to clear the file before writing
    # with open(file_name, "w") as file:
    #     file.write("")  # clear the file

    # Read and write all the source codes of the project to a file
    apps_folder = os.path.join(base_dir, "apps")
    core_folder = os.path.join(base_dir, "core")
    utils_folder = os.path.join(base_dir, "utils")

    write_source_code_inside_folder(apps_folder)
    write_source_code_inside_folder(core_folder)
    print("Done!")
