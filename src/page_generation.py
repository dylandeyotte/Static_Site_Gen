import os
import shutil
from markdown import markdown_to_html_node, extract_title

def copy_contents(source, destination):
    list_dir = os.listdir(source)
    for item in list_dir:
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        else:
            new_dest = os.path.join(destination, item)
            os.makedirs(new_dest, exist_ok=True)
            copy_contents(item_path, new_dest)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r') as f:
        md_file = f.read()
    with open(template_path, 'r') as f:
        template_file = f.read()
    
    node = markdown_to_html_node(md_file)
    html_string = node.to_html()
    title = extract_title(md_file)

    new_html = template_file.replace('{{ Title }}', title).replace('{{ Content }}', html_string)
    new_html = new_html.replace('href="/', f'href="{basepath}').replace('src="/', 'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(new_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        dest_path = os.path.join(dest_dir_path, item)   
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path) and item_path.endswith('.md'):
            new_dest = dest_path.strip('md') + 'html'
            generate_page(item_path, template_path, new_dest, basepath)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(item_path, template_path, dest_path, basepath)


