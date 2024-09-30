import os
import shutil

def copy_files_recursive(source_diretory_path, destiny_directory_path):
    if not os.path.exists(destiny_directory_path):
        os.mkdir(destiny_directory_path)

    for filename in os.listdir(source_diretory_path):
        from_path = os.path.join(source_diretory_path, filename)
        dest_path = os.path.join(destiny_directory_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)