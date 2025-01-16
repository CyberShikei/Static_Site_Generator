import unittest

from src.node.html.leaf import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        TEST_TAG = "a"

        node = LeafNode(TEST_TAG, "This is a span")
        node2 = LeafNode("a", "This is a span")

        self.assertEqual(node, node2)

    def test_eq_false(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG, "This is a span")
        node2 = LeafNode(TEST_TAG, "This is a div")

        self.assertNotEqual(node, node2)

    def test_repr(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG, "This is a span")
        t_str = """LeafNode(
        tag=a,
        value=This is a span,
        props={}
)"""

        self.assertEqual(repr(node), t_str)

    def test_props_to_html(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG, "This is a span",
                        props={"class": "container"})
        t_str = ' class="container"'

        self.assertEqual(node.props_to_html(), t_str)

    def test_props_to_html_empty(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG, "This is a span")
        t_str = ""

        self.assertEqual(node.props_to_html(), t_str)

    def test_props_to_html_multiple(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG,
                        "This is a span", props={"class": "container",
                                                 "id": "main"})
        t_str = ' class="container" id="main"'

        self.assertEqual(node.props_to_html(), t_str)

    # LeafNode can't have children
    def test_cant_have_children(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG, "This is a span")
        # node.children = ["This is a child"]
        t_str = None

        self.assertEqual(node.children, t_str)

    def test_to_html(self):
        TEST_TAG = "a"
        node = LeafNode(TEST_TAG, "This is a span")
        t_str = "<a>This is a span</a>"
        self.assertEqual(node.to_html(), t_str)
