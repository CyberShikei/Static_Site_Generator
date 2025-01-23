import unittest

from src.convert.markdown_to_html_node import md_to_html_nodes

# TODO: FIX THIS TEST OR WHAT IT'S TESTING


class TestMDToHTMLNode(unittest.TestCase):
    def test_md_to_html_nodes(self):
        markdown = "# Hello, World!"
        parent_node = md_to_html_nodes(markdown)
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "h1")
        self.assertEqual(parent_node.children[0].value, "Hello, World!")

    def test_md_to_html_nodes_paragraph(self):
        markdown = "Hello, World!"
        parent_node = md_to_html_nodes(markdown)
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].children[0].tag, "")
        message = f"____GOT {parent_node.children[0]}____"
        self.assertEqual(
            parent_node.children[0].children[0].value,
            "Hello, World!",
            message)

    def test_md_to_html_nodes_code(self):
        markdown = "```python\nprint('Hello, World!')\n```"
        parent_node = md_to_html_nodes(markdown)
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "code")
        self.assertEqual(
            parent_node.children[0].value, "python\nprint('Hello, World!')\n")

    def test_md_to_html_nodes_ordered_list(self):
        markdown = """1. Hello\n2. World"""
        parent_node = md_to_html_nodes(markdown)

        message = f"____GOT {parent_node}____"

        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "ol")
        self.assertEqual(len(parent_node.children[0].children),
                         2,
                         message)
        self.assertEqual(parent_node.children[0].children[0].value, "Hello")
        self.assertEqual(parent_node.children[0].children[1].value, "World")

    def test_md_to_html_nodes_unordered_list(self):
        markdown = """* Hello\n* World"""
        parent_node = md_to_html_nodes(markdown)
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children[0].children),
                         2)
        self.assertEqual(parent_node.children[0].children[0].value, "Hello")
        self.assertEqual(parent_node.children[0].children[1].value, "World")

    def test_md_to_html_nodes_quote(self):
        markdown = "> Hello, World!"
        parent_node = md_to_html_nodes(markdown)
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].tag, "q")
        self.assertEqual(parent_node.children[0].value, "Hello, World!")

    def test_md_to_html_nodes_multi_markdown(self):
        markdown = """# Hello, World!
        ```Testing
        code
        print('Hello, World!')
        ```

        * Hello
        * World

        > Hello, World!
        
        paragraph of text

        ### Heading level 3

        """

        parent_node = md_to_html_nodes(markdown)

        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(len(parent_node.children), 6)
        self.assertEqual(parent_node.children[0].tag, "h1")
        self.assertEqual(parent_node.children[1].tag, "code")
        self.assertEqual(parent_node.children[2].tag, "ul")
        self.assertEqual(parent_node.children[3].tag, "q")
        self.assertEqual(parent_node.children[4].tag, "p")
        self.assertEqual(parent_node.children[5].tag, "h3")


# def __casing(test_text: str, test_case: str) -> str:
