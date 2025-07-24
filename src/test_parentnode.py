import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_nested_parentnodes(self):
        inner = ParentNode("span", children=[LeafNode("b", "Bold")])
        outer = ParentNode("div", children=[inner])
        expected_html = "<div><span><b>Bold</b></span></div>"
        self.assertEqual(outer.to_html(), expected_html)
