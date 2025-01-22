import unittest

from src.convert import text_to_html
from src.nodes import TextNode, TextType
from src.nodes.html.node import HTMLNode


class TestTextToHtml(unittest.TestCase):
    def test_text_to_html_no_tag(self):
        TEXT = "Hello, World!"
        TEXT_TYPE = TextType.NORMAL
        URL = "https://www.google.com"

        node_args = (TEXT, TEXT_TYPE, URL)
        text_node = TextNode(*node_args)

        html_node = text_to_html(text_node)

        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, TEXT)

    def test_text_to_html_bold(self):
        TEXT = "Hello, World!"
        TEXT_TYPE = TextType.BOLD
        URL = "https://www.google.com"

        node_args = (TEXT, TEXT_TYPE, URL)
        text_node = TextNode(*node_args)

        html_node = text_to_html(text_node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, TEXT)

    def test_text_to_html_italic(self):
        TEXT = "Hello, World!"
        TEXT_TYPE = TextType.ITALIC
        URL = "https://www.google.com"

        node_args = (TEXT, TEXT_TYPE, URL)
        text_node = TextNode(*node_args)

        html_node = text_to_html(text_node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, TEXT)

    def test_text_to_html_code(self):
        TEXT = "Hello, World!"
        TEXT_TYPE = TextType.CODE
        URL = "https://www.google.com"

        node_args = (TEXT, TEXT_TYPE, URL)
        text_node = TextNode(*node_args)

        html_node = text_to_html(text_node)

        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, TEXT)

    def test_text_to_html_link(self):
        TEXT = "Hello, World!"
        TEXT_TYPE = TextType.LINK
        URL = "https://www.google.com"

        node_args = (TEXT, TEXT_TYPE, URL)
        text_node = TextNode(*node_args)

        html_node = text_to_html(text_node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, TEXT)
        self.assertEqual(html_node.props["href"], URL)

    def test_text_to_html_image(self):
        TEXT = "Hello, World!"
        TEXT_TYPE = TextType.IMAGE
        URL = "https://www.google.com"

        node_args = (TEXT, TEXT_TYPE, URL)
        text_node = TextNode(*node_args)

        html_node = text_to_html(text_node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], URL)
        self.assertEqual(html_node.props["alt"], TEXT)
