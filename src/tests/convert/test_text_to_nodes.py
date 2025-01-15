import unittest

from src.convert.text_to_nodes import text_to_textnodes
from src.nodes.text import TextNode
from src.nodes.types import TextType


class TestTextToNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = 'init text'
        text += '[testing limk](https://www.testing.link)'
        text += '![testing image](https://www.testing.image)'
        text += ' leie `testing code`'
        text += ' sad **testing bold** bold is good '
        text += '*testing italic* help me!!! '
        text += 'This is text with a link'

        expected_out = [
            TextNode('init text', TextType.NORMAL),
            TextNode('testing limk', TextType.LINK,
                     'https://www.testing.link'),
            TextNode('testing image', TextType.IMAGE,
                     'https://www.testing.image'),
            TextNode(' leie ', TextType.NORMAL),
            TextNode('testing code', TextType.CODE),
            TextNode(' sad ', TextType.NORMAL),
            TextNode('testing bold', TextType.BOLD),
            TextNode(' bold is good ', TextType.NORMAL),
            TextNode('testing italic', TextType.ITALIC),
            TextNode(' help me!!! This is text with a link', TextType.NORMAL)
        ]

        result = text_to_textnodes(text)

        err_msg = f"""Expected {expected_out},

        but got {result}"""

        self.assertEqual(result, expected_out, err_msg)

    def test_text_to_textnodes_two(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        result = text_to_textnodes(text)

        err_msg = f"""Expected {expected},

        but got {result}"""

        self.assertEqual(result, expected, err_msg)


if __name__ == '__main__':
    unittest.main()
