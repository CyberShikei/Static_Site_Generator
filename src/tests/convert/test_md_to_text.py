import unittest

from src.convert.md_to_text import split_nodes_delimiter
from src.textnode import TextType, TextNode


class TestMdToText(unittest.TestCase):
    # Examples:
    #
    #       This is text with a **bolded phrase** in the middle

    # the text above should become the following:
    #
    #       [
    #           TextNode("This is text with a ", TextType.TEXT),
    #           TextNode("bolded phrase", TextType.BOLD),
    #           TextNode(" in the middle", TextType.TEXT),
    #       ]

    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("**", TextType.BOLD),
            TextNode("bolded phrase", TextType.TEXT),
            TextNode("**", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("", TextType.BOLD),
                TextNode("bolded phrase", TextType.TEXT),
                TextNode("", TextType.BOLD),
                TextNode(" in the middle", TextType.TEXT),
            ],
        )
