import unittest

from src.nodes.html.node import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        TEST_TAG = "i"

        node = HTMLNode(TEST_TAG, "This is a div")
        node2 = HTMLNode(TEST_TAG, "This is a div")

        self.assertEqual(node, node2)

    def test_eq_false(self):
        TEST_TAG = "i"

        node = HTMLNode(TEST_TAG, "This is a div")
        node2 = HTMLNode(TEST_TAG, "This is a span")

        self.assertNotEqual(node, node2)

    def test_repr(self):
        TEST_TAG = "i"

        node = HTMLNode(TEST_TAG, "This is a div")
        t_str = """HTMLNode(
        tag=i,
        value=This is a div,
        props={},
        children=[]
)"""

        self.assertEqual(repr(node), t_str)

    def test_props_to_html(self):
        TEST_TAG = "i"

        node = HTMLNode(TEST_TAG,
                        "This is a div",
                        props={"class": "container"})
        t_str = 'class="container"'

        self.assertEqual(node.props_to_html(), t_str)

    def test_props_to_html_empty(self):
        TEST_TAG = "i"

        node = HTMLNode(TEST_TAG, "This is a div")
        t_str = ""

        self.assertEqual(node.props_to_html(), t_str)

    def test_props_to_html_multiple(self):
        TEST_TAG = "i"

        node = HTMLNode(TEST_TAG,
                        "This is a div", props={"class": "container",
                                                "id": "main"})
        t_str = 'class="container" id="main"'

        self.assertEqual(node.props_to_html(), t_str)


if __name__ == "__main__":
    unittest.main()
