import unittest
import pytest

from src.convert.nodes import ParentNode
from src.convert.nodes import LeafNode


class TestParentNode(unittest.TestCase):

    def test_init(self):
        # Arrange
        tag = "h2"
        children = [ParentNode(tag="p",
                               children=[],
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
        tag = "h1"
        leaf_children = [LeafNode("i", "This is a span"),
                         LeafNode("code", "This is another span"),
                         LeafNode("b", "This is a third span")]
        children = [ParentNode(tag="p", children=leaf_children, props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        result = node.to_html()

        lefs = [leaf.to_html() for leaf in leaf_children]

        equals = f'<h1 id="main"><p>{lefs[0]}{lefs[1]}{lefs[2]}</p></h1>'

        # Assert
        self.assertEqual(result, equals)

    def test_to_html_no_tag(self):
        # Arrange
        tag = ""
        leaf = LeafNode("a", "This is a span")
        children = [ParentNode(tag="p", children=[leaf], props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        with pytest.raises(ValueError):
            node = ParentNode(*targs)
            node.to_html()

    def test_to_html_no_children(self):
        # Arrange
        tag = "h5"

        children = []
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        with pytest.raises(ValueError):
            node = ParentNode(*targs)
            node.to_html()

    def test_nested_parents_to_html(self):
        # Arrange
        tag = "h1"
        leaf_children = [LeafNode("i", "This is a span"),
                         ParentNode("p", [LeafNode("i", "This is a span"),
                                          LeafNode(
                                              "code", "This is another span")
                                          ],
                                    {})
                         ]

        children = [ParentNode(tag="p",
                               children=leaf_children,
                               props={})
                    ]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        result = node.to_html()

        equals = f'<h1 id="main"><p>{leaf_children[0].to_html()}<p>{leaf_children[1].children[0].to_html()}{
            leaf_children[1].children[1].to_html()}</p></p></h1>'

        # Assert
        self.assertEqual(result, equals)

    def test_eq(self):
        # Arrange
        tag = "h4"
        children = [ParentNode(tag="p",
                               children=[],
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
        tag = "h3"
        children = [ParentNode(tag="p",
                               children=[],
                               props={})]
        props = {"id": "main"}

        targs = (tag, children, props)

        # Act
        node = ParentNode(*targs)
        node2 = ParentNode("h4", children, props)

        # Assert
        self.assertNotEqual(node, node2)

    def test_repr(self):
        # Arrange
        tag = "h1"
        children = [ParentNode(tag="p",
                               children=[],
                               props={})
                    ]
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
