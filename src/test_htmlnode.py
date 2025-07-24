import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value="link",
            props={"href": "https://example.com", "class": "external"},
        )
        html = node.props_to_html()
        self.assertIn('href="https://example.com"', html)
        self.assertIn('class="external"', html)
        self.assertTrue(html.startswith(" href="))
        self.assertTrue(html.endswith('"'))

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", value="content", props={})
        html = node.props_to_html()
        self.assertEqual(html, "")

    def test_props_to_html_special_chars(self):
        node = HTMLNode(
            tag="img", value=None, props={"src": "image.png", "alt": 'A "quote"'}
        )
        html = node.props_to_html()
        self.assertIn('src="image.png"', html)
        self.assertIn('alt="A "quote""', html)


if __name__ == "__main__":
    unittest.main()
