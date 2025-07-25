from textnode import TextNode, TextType

# TODO: Nested inline elements like "_**bold** inside italic_"

from splitnodes import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

if __name__ == "__main__":
    main()
