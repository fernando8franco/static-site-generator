import os
import shutil
from copystatic import copy_files_recursive
from textnode import TextNode


directory_path_static = "./static"
directory_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(directory_path_public):
        shutil.rmtree(directory_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(directory_path_static, directory_path_public)

if __name__ == "__main__":
    main()