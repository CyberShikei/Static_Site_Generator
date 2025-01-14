import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)

        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        t_str = "TextNode(This is a text node, bold, None)"

        self.assertEqual(repr(node), t_str)

    def test_enforce_type(self):
        node = TextNode("This is a text node", "bold")

        self.assertEqual(node.text_type, TextType.BOLD)

    def test_enforce_type_invalid(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", "invalid")


if __name__ == "__main__":
    unittest.main()
