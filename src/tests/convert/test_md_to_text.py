import unittest

from src.convert.md_to_text import split_nodes_delimiter
from src.textnode import TextType, TextNode


class TestMdToText(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("Hello", TextType.NORMAL),
                 TextNode("world", TextType.BOLD)]

        delimiter = "**"

        text_type = TextType.BOLD

        expected = [TextNode("Hello", TextType.NORMAL), TextNode(
            "", text_type), TextNode("world", TextType.BOLD)]

        self.assertEqual(split_nodes_delimiter(
            nodes, delimiter, text_type), expected)
