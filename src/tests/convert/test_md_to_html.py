import unittest

from src.convert.markdown_to_html_node import markdown_to_html_node

from src.nodes.html.node import HTMLNode
from src.nodes.html.leaf import LeafNode
from src.nodes.html.parent import ParentNode

CASES = {
    "CODE": {
        # PURE CODE
        "```python\nprint('Hello, World!')\n```":
            [LeafNode("code", "python\nprint('Hello, World!')\n")],
        "```python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n```":
            [LeafNode(
                "code", "python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n")],
        "```python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n\n```":
            [LeafNode(
                "code", "python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n")],
        "```python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n\n```":
            [LeafNode(
                "code", "python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n\n")],

        # CODE IN PARAGRAPH
        "This is a code block: ```python\nprint('Hello, World!')\n```":
            [LeafNode("", "This is a code block: "),
             LeafNode("code", "python\nprint('Hello, World!')\n")],
        "This is a code block: ```python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n```":
            [LeafNode("", "This is a code block: "),
             LeafNode("code", "python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n")],
        "This is a code block: ```python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n\n```":
            [LeafNode("", "This is a code block: "),
             LeafNode("code", "python\nprint('Hello, World!')\n\nprint('Goodbye, World!')\n")],
    },
}


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = "This is **text** with an *italic* word "
        markdown += "and a `code block` and "
        markdown += "an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
        markdown += "and a [link](https://boot.dev)"

        html_nodes = markdown_to_html_node(markdown)

        expected = [
            LeafNode("", "This is "),
            LeafNode("b", "text"),
            LeafNode("", " with an "),
            LeafNode("i", "italic"),
            LeafNode("", " word and a "),
            LeafNode("code", "code block"),
            LeafNode("", " and an "),
            LeafNode("img", props={"src": "https://i.imgur.com/fJRm4Vk.jpeg",
                                   "alt": "obi wan image"}),
            LeafNode("", " and a "),
            LeafNode("a", props={"href": "https://boot.dev"}, value="link")
        ]

        err_msg = f"""Expected {expected},

        but got {html_nodes}"""

        self.assertEqual(html_nodes, expected, err_msg)

    def test_markdown_to_html_node_code(self):
        for case, expected in CASES["CODE"].items():
            with self.subTest(case=case):
                html_nodes = markdown_to_html_node(case)
                err_msg = err_message(case, expected, html_nodes)
                self.assertEqual(html_nodes, expected, err_msg)


def err_message(case, expected, html_nodes):
    return f"""\n-------------------
    Case:
        {case}
===================
    Expected:
        {expected}
===================
    BUT GOT:
        {html_nodes}"""
