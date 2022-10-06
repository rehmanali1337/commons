import os


def read_txt_lines(file: str):
    lines = open(file, encoding="UTF-8").readlines()
    return [line.strip() for line in lines if line.strip() != ""]


def files_in_folder(folder: str):
    for path, dirnames, filenames in os.walk(folder):
        break
    return [f"{path}/{filename}" for filename in filenames]


def create_txt_file(file: str):
    if not os.path.exists(file):
        with open(file, "w", encoding="UTF-8"):
            pass
