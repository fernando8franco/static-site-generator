import os
import shutil

from markdown_blocks import extract_title, markdown_to_html_node

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

def generate_page(from_path, template_path, dest_path):
    print(f"Generationg page from {from_path} to {dest_path} using {template_path}")

    for filename in os.listdir(from_path):
        file_path = os.path.join(from_path, filename)
        file_dest_path = os.path.join(dest_path, filename)
        if os.path.isfile(file_path):
            file = open(file_path, "r")
            markdown = file.read()
            file.close
            file = open(template_path, "r")
            template = file.read()
            file.close
            content = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
            open(f"{file_dest_path[:-3]}.html", "x")
            file = open(f"{file_dest_path[:-3]}.html", "w")
            file.write(page)
            file.close()
        else:
            os.makedirs(file_dest_path)
            generate_page(file_path, template_path, file_dest_path)