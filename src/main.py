import os
import sys
import shutil
from page_generation import copy_contents, generate_page, generate_pages_recursive

basepath = sys.argv[1] if len(sys.argv) > 1 else '/'

def main():

    source = './static'
    destination = './docs'
    template = './template.html'
    content = './content'

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)

    copy_contents(source, destination)

    generate_pages_recursive(content, template, destination, basepath)
    
# http://localhost:8888
main()


