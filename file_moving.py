import os
import shutil
from pathlib import Path

def move_files(source_folder):

    files = os.listdir(source_folder)

    for file in files:
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):

            file_extension = Path(file).suffix
            destination_folder = os.path.join(source_folder, file_extension[1:].upper() + "_Files")

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)
            print(f"Moved {file} to {destination_path}")

source_folder = '/home/devum/files'
move_files(source_folder)
