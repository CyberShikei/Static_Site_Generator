import unittest

from src.convert.md_to_text import split_nodes_delimiter
from src.nodes.types import TextType
from src.nodes.text import TextNode


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
        old_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("**bolded phrase**", TextType.NORMAL),
            TextNode(" in the middle", TextType.NORMAL),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "**")

        expected_out = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.NORMAL),
        ]

        err_msg = f"""Expected {expected_out},

        but got {new_nodes}"""

        self.assertEqual(new_nodes, expected_out, err_msg)

    def test_split_nodes_italic(self):
        old_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("*italic phrase*", TextType.NORMAL),
            TextNode(" in the middle", TextType.NORMAL),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "*")

        expected_out = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.NORMAL),
        ]

        err_msg = f"""Expected {expected_out},

        but got {new_nodes}"""

        self.assertEqual(new_nodes, expected_out, err_msg)

    def test_split_nodes_code(self):
        old_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("`code phrase`", TextType.NORMAL),
            TextNode(" in the middle", TextType.NORMAL),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "`")

        expected_out = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code phrase", TextType.CODE),
            TextNode(" in the middle", TextType.NORMAL),
        ]

        err_msg = f"""Expected {expected_out},

        but got {new_nodes}"""

        self.assertEqual(new_nodes, expected_out, err_msg)


def main():
    unittest.main()
