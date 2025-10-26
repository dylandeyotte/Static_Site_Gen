from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    splitlist = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            splitlist.append(node)
            continue
        split_node = node.text.split(delimiter)
        new_node = []
        if len(split_node) % 2 == 0:
            raise ValueError('Invalid syntax')
        for entry in split_node:
            if entry == '':
                continue
            if split_node.index(entry) % 2 == 0:
                new_node.append(TextNode(entry, TextType.TEXT))
            else:
                new_node.append(TextNode(entry, text_type))
        splitlist.extend(new_node)
    return splitlist


def extract_markdown_images(text):
    matches = re.findall(r'!\[(.*?)\]\((.*?)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'\[(.*?)\]\((.*?)\)', text)
    return matches


def split_nodes_image(old_nodes):
    final = []  
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final.append(node)
            continue
        text = node.text
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            final.append(node)
            continue
        for i in links:
            split_node = text.split(f"![{i[0]}]({i[1]})", 1)
            if len(split_node) != 2:
                raise ValueError('Invalid syntax')
            if split_node[0] != '':
                final.append(TextNode(split_node[0], TextType.TEXT))
            final.append(TextNode(i[0], TextType.IMAGE, i[1]))
            text = split_node[1]
        if text != '':
            final.append(TextNode(text, TextType.TEXT))
    return final

def split_nodes_link(old_nodes):
    final = []  
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final.append(node)
            continue
        text = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            final.append(node)
            continue
        for i in links:
            split_node = text.split(f"[{i[0]}]({i[1]})", 1)
            if len(split_node) != 2:
                raise ValueError('Invalid syntax')
            if split_node[0] != '':
                final.append(TextNode(split_node[0], TextType.TEXT))
            final.append(TextNode(i[0], TextType.LINK, i[1]))
            text = split_node[1]
        if text != '':
            final.append(TextNode(text, TextType.TEXT))
    return final

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_delimiter(node, '**', TextType.BOLD)
    node = split_nodes_delimiter(node, '_', TextType.ITALIC)
    node = split_nodes_delimiter(node, '`', TextType.CODE)
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    return node

