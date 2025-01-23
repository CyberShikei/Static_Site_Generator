import pytest

from src.convert.nodes import TextNode, TextType


class TestTextNode():
    def test_text_node(self):
        text = "Hello World"
        url = "https://example.com"
        text_type = TextType.NORMAL
        node = TextNode(text, text_type, url)

        assert node.text == text
        assert node.url == url
        assert node.text_type == text_type

    def test_text_node_repr(self):
        text = "Hello World"
        url = "https://example.com"
        text_type = TextType.NORMAL
        node = TextNode(text, text_type, url)

        assert repr(node) == f"TextNode({text}, {text_type}, {url})"

    def test_text_node_eq(self):
        text = "Hello World"
        url = "https://example.com"
        text_type = TextType.NORMAL
        node1 = TextNode(text, text_type, url)
        node2 = TextNode(text, text_type, url)

        assert node1 == node2

    def test_text_node_text_type(self):
        text = "Hello World"
        url = "https://example.com"
        text_type = TextType.TEXT
        node = TextNode(text, text_type, url)

        assert node.text_type == TextType.NORMAL
        assert node.text == text
        assert node.url == url
        assert node.text_type == TextType.NORMAL
