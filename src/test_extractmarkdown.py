import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_images_empty_alt_text(self):
        matches = extract_markdown_images(
            "Check out this ![](https://example.com/image.jpg)"
        )
        self.assertListEqual([("", "https://example.com/image.jpg")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "First ![photo](img1.png) and second ![diagram](img2.jpg)"
        )
        self.assertListEqual([("photo", "img1.png"), ("diagram", "img2.jpg")], matches)

    def test_extract_markdown_links_empty_text(self):
        matches = extract_markdown_links("Visit [](https://github.com) for code")
        self.assertListEqual([("", "https://github.com")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "Go to [Google](https://google.com) or [GitHub](https://github.com)"
        )
        self.assertListEqual(
            [("Google", "https://google.com"), ("GitHub", "https://github.com")],
            matches,
        )
