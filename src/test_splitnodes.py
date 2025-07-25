import unittest
from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter_with_bold_delimiter(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_with_italic_delimiter(self):
        nodes = [TextNode("This is _italic_ text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_with_code_delimiter(self):
        nodes = [TextNode("Here is `code` sample", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("Here is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" sample", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_with_multiple_delimiters(self):
        nodes = [TextNode("**bold** and _italic_", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC)
        self.assertEqual(
            result,
            [
                TextNode("", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode("", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_with_no_delimiter(self):
        nodes = [TextNode("No delimiter here", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("No delimiter here", TextType.TEXT)])


if __name__ == "__main__":
    unittest.main()
