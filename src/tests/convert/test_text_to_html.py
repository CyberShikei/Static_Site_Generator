import unittest

from src.convert.text_to_html import text_to_html, text_type_to_html_tag
from src.textnode import TextNode, TextType
from src.html.node import HTMLNode


class TestTextToHtml(unittest.TestCase):
    def test_text_to_html(self):
        txt_test_type = TextType.IMAGE
        txt_test_text = "Test Text"
        txt_test_url = "http://test.com"

        txt_node = TextNode(txt_test_text, txt_test_type, txt_test_url)

        html_tag = 'IMG'
        html_value = txt_test_text
        html_children = []
        html_props = {}

        expected = HTMLNode(tag=html_tag, value=html_value,
                            children=html_children, props=html_props)

        result = text_to_html(txt_node)

        self.assertEqual(result, expected)

    def test_text_type_to_html_tag(self):
        txt_test_type = TextType.IMAGE

        result = text_type_to_html_tag(txt_test_type).value

        self.assertEqual(result, 'IMG')

    def test_text_type_to_html_tag_invalid(self):
        txt_test_type = 'invalid'

        with self.assertRaises(ValueError):
            text_type_to_html_tag(txt_test_type)
