from textnode import TextNode, TextType

# TODO: Nested inline elements like "_**bold** inside italic_"

from splitnodes import split_nodes_delimiter
from texttotextnodes import text_to_textnodes


def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = text_to_textnodes("This is **text** _with_ ![bruh](moment.com)")
    print(new_nodes)


if __name__ == "__main__":
    main()
