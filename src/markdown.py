from blocks import block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode, HTMLNode
from conversions import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_blocks(markdown):
    final = []
    split_lines = markdown.split('\n\n')
    for line in split_lines:
        if line != '':
            final.append(line.strip())
    return final
    
def text_to_children(text):
    node_list = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        node_list.append(text_node_to_html_node(node))
    return node_list

def paragraph_to_node(block):
    split_block = block.split('\n')
    final = ' '.join(split_block)
    return ParentNode('p', children=text_to_children(final))

def heading_to_node(block):
    hash_amt = block.find(' ')
    if hash_amt > 6:
        raise ValueError('Invalid heading')
    children = text_to_children(block[hash_amt+1:])
    return ParentNode(f'h{hash_amt}', children)

def code_to_node(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError('Invalid code')
    clean_block = block.strip('```').lstrip('\n')
    return ParentNode('pre', [LeafNode('code', clean_block)])

def quote_to_node(block):
    node_list= []
    split_block = block.split('\n')
    for line in split_block:
        node_list.append(line.strip('> '))
    final = ' '.join(node_list)
    return ParentNode('blockquote', children=text_to_children(final))

def unordered_list_to_node(block):
    lines = block.split('\n')
    children = []
    for line in lines:
        strip_line = line.strip('- ')
        children.append(ParentNode('li', text_to_children(strip_line)))
    return ParentNode('ul', children)

def ordered_list_to_node(block):
    num = 1
    lines = block.split('\n')
    children = []
    for line in lines:
        strip_line = line.strip(f'{num}. ')
        num += 1
        children.append(ParentNode('li', text_to_children(strip_line)))
    return ParentNode('ol', children)


def markdown_to_html_node(markdown):
    big_list = []
    split_block = markdown_to_blocks(markdown)
    for block in split_block:
        if block_to_block_type(block) == BlockType.HEADING:
            big_list.append(heading_to_node(block))
        elif block_to_block_type(block) == BlockType.PARAGRAPH:
            big_list.append(paragraph_to_node(block))
        elif block_to_block_type(block) == BlockType.CODE:  
            big_list.append(code_to_node(block))
        elif block_to_block_type(block) == BlockType.QUOTE:
            big_list.append(quote_to_node(block))
        elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
            big_list.append(unordered_list_to_node(block))
        elif block_to_block_type(block) == BlockType.ORDERED_LIST:
            big_list.append(ordered_list_to_node(block))
    return ParentNode('div', children=big_list)
 
def extract_title(markdown):
    if not markdown.startswith('#'):
        raise ValueError('Invalid syntax')
    lines = markdown.split('\n')
    for line in lines:
        new_md = line.strip('#').strip()
    return new_md



