import unittest

from markdowntoblocks import markdown_to_blocks
from src.markdowntoblocks import BlockType, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraph_block(self):
        """Test that regular text is identified as paragraph"""
        block = "This is a regular paragraph with some text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = "This is a paragraph\nwith multiple lines\nthat don't match any special format."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_blocks(self):
        """Test heading identification with 1-6 # characters"""
        # Valid headings
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

        # Invalid headings (# not at start)
        self.assertEqual(block_to_block_type("Not # a heading"), BlockType.PARAGRAPH)

    def test_code_blocks(self):
        """Test code block identification"""
        # Valid code blocks
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = "```python\ndef function():\n    pass\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        # Invalid code blocks (missing closing backticks)
        block = "```\nprint('hello')"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        # Invalid code blocks (missing opening backticks)
        block = "print('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_blocks(self):
        """Test quote block identification"""
        # Valid quote blocks
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = "> This is a quote\n> with multiple lines\n> all starting with >"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        # Invalid quote blocks (missing > on some lines)
        block = "> This is a quote\nBut this line doesn't start with >"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_blocks(self):
        """Test unordered list identification"""
        # Valid unordered lists
        block = "- Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.UL)

        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UL)

        # Invalid unordered lists (missing - on some lines)
        block = "- Item 1\nNot a list item\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_blocks(self):
        """Test ordered list identification"""
        # Valid ordered lists
        block = "1. Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.OL)

        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.OL)

        # Invalid ordered lists (wrong starting number)
        block = "2. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        # Invalid ordered lists (non-sequential numbers)
        block = "1. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        # Invalid ordered lists (missing space after .)
        block = "1.No space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        # Invalid ordered lists (no . after number)
        block = "1 Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
