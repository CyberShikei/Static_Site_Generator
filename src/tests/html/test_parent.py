import unittest
import pytest

from src.html.parent import ParentNode
from src.html.leaf import LeafNode


class TestParentNode(unittest.TestCase):

    def test_init(self):
        # Arrange
        tag = "div"
        children = [ParentNode(tag="p",
                               children=[LeafNode("span",
                                                  "This is a span")],
                               props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)

        # Assert
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_to_html(self):
        # Arrange
        tag = "div"
        leaf_children = [LeafNode("span", "This is a span"),
                         LeafNode("span", "This is another span"),
                         LeafNode("span", "This is a third span")]
        children = [ParentNode(tag="p", children=leaf_children, props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        result = node.to_html()

        lefs = [leaf.to_html() for leaf in leaf_children]

        equals = f'<div id="main"><p>{lefs[0]}{lefs[1]}{lefs[2]}</p></div>'

        # Assert
        self.assertEqual(result, equals)

    def test_to_html_no_tag(self):
        # Arrange
        tag = ""
        leaf = LeafNode("span", "This is a span")
        children = [ParentNode(tag="p", children=[leaf], props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        with pytest.raises(ValueError):
            node = ParentNode(*targs)
            node.to_html()

    def test_to_html_no_children(self):
        # Arrange
        tag = "div"

        children = []
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        with pytest.raises(ValueError):
            node = ParentNode(*targs)
            node.to_html()

    def test_eq(self):
        # Arrange
        tag = "div"
        children = [ParentNode(tag="p",
                               children=[LeafNode("span",
                                                  "This is a span")],
                               props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        node2 = ParentNode(*targs)

        # Assert
        self.assertEqual(node, node2)

    def test_eq_false(self):
        # Arrange
        tag = "div"
        children = [ParentNode(tag="p",
                               children=[LeafNode("span",
                                                  "This is a span")],
                               props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        node2 = ParentNode("div", [], {})

        # Assert
        self.assertNotEqual(node, node2)

    def test_repr(self):
        # Arrange
        tag = "div"
        children = [ParentNode(tag="p",
                               children=[LeafNode("span",
                                                  "This is a span")],
                               props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        t_str = f"""ParentNode(
        tag={tag},
        children={children},
        props={props}
)"""

        # Assert
        self.assertEqual(repr(node), t_str)
