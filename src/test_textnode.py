import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("I don't have a url", TextType.TEXT, None)
        node2 = TextNode("I don't have a url", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node bruh", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_plain_text(self):
        tn = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(tn)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")

    def test_link_text(self):
        tn = TextNode("GitHub", TextType.LINK, "https://github.com")
        html_node = text_node_to_html_node(tn)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "GitHub")
        self.assertEqual(html_node.props, {"href": "https://github.com"})


if __name__ == "__main__":
    unittest.main()
