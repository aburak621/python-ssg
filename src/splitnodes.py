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
