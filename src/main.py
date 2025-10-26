import os
import shutil
from page_generation import copy_contents, generate_page, generate_pages_recursive

def main():

    source = './static'
    destination = './public'
    template = './template.html'
    content = './content'

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)

    copy_contents(source, destination)

    generate_pages_recursive(content, template, destination)
    
# http://localhost:8888
main()
