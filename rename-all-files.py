# This script renames all files in a directory for a specified file extension.
# In sequence, the files will be renamed as 1.jpg, 2.jpg, 3.jpg, etc.
import os

def rename_files(directory_path, file_extension):
    os.chdir(directory_path)
    files = os.listdir()
    target_files = [file for file in files if file.endswith(".webm")]

    for index, file in enumerate(target_files, start=1):
        new_name = f"{index}{file_extension}"
        os.rename(file, new_name)
        print(f"Renamed: {file} -> {new_name}")

directory_path = '/path/to/directory'
rename_files(directory_path, file_extension=".webm")
