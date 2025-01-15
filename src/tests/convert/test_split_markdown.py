import unittest

from src.convert.split_markdown import split_nodes_link, split_nodes_image
from src.nodes.text import TextNode
from src.nodes.types import TextType


class TestSplitMarkdown(unittest.TestCase):
    def test_split_nodes_link(self):
        # Input node with mixed text and Markdown-style links
        input_node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        # Expected output nodes with links extracted
        expected_output = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]

        # Extract links from input node
        new_nodes = split_nodes_link([input_node])

        # Check if the output nodes match the expected output
        message = f"""
        Input node: {input_node}

        Expected output: {expected_output}

        Output nodes: {new_nodes}
        """

        self.assertEqual(new_nodes, expected_output, message)

    def test_split_nodes_image(self):
        # Input node with mixed text and Markdown-style images
        input_node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )

        # Expected output nodes with images extracted
        expected_output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE,
                     "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE,
                     "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]

        # Extract images from input node
        new_nodes = split_nodes_image([input_node])

        # Check if the output nodes match the expected output
        message = f"""
        Input node: {input_node}

        Expected output: {expected_output}

        Output nodes: {new_nodes}
        """

        self.assertEqual(new_nodes, expected_output, message)


if __name__ == "__main__":
    unittest.main()
