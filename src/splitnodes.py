from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        inside_delimiter = False
        strings = old_node.text.split(delimiter)
        for string in strings:
            if inside_delimiter:
                nodes.append(TextNode(string, text_type))
            else:
                nodes.append(TextNode(string, TextType.TEXT))
            inside_delimiter = not inside_delimiter
    return nodes


def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        matches = extract_markdown_images(old_node.text)

        if len(matches) == 0:
            nodes.append(old_node)

        node_text = old_node.text
        for index, match in enumerate(matches):
            sections = node_text.split(f"![{match[0]}]({match[1]})", 1)
            node_text = sections[1]
            nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            if index == len(matches) - 1:
                if len(sections[1]) != 0:
                    nodes.append(TextNode(sections[1], TextType.TEXT))
    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue

        matches = extract_markdown_links(old_node.text)

        if len(matches) == 0:
            nodes.append(old_node)

        node_text = old_node.text
        for index, match in enumerate(matches):
            sections = node_text.split(f"[{match[0]}]({match[1]})", 1)
            node_text = sections[1]
            nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if index == len(matches) - 1:
                if len(sections[1]) != 0:
                    nodes.append(TextNode(sections[1], TextType.TEXT))
    return nodes
