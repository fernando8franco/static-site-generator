import os
import shutil
from copystatic import copy_files_recursive, generate_page

directory_path_static = "./static"
directory_path_public = "./public"
directory_path_content = "./content"
path_template = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(directory_path_public):
        shutil.rmtree(directory_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(directory_path_static, directory_path_public)

    generate_page(directory_path_content, path_template, directory_path_public)

if __name__ == "__main__":
    main()