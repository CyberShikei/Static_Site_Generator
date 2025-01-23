import unittest

from src.convert import block_to_block_type
from src.convert.nodes import BlockType

CASES = [
    ("# Heading", BlockType.H1),
    ("## Heading", BlockType.H2),
    ("### Heading", BlockType.H3),
    ("#### Heading", BlockType.H4),
    ("##### Heading", BlockType.H5),
    ("###### Heading", BlockType.H6),
    ("```", BlockType.CODE),
    ("1. List", BlockType.ORDERED_LIST),
    ("- List", BlockType.UNORDERED_LIST),
    ("* List", BlockType.UNORDERED_LIST),
    ("> Quote", BlockType.QUOTE),
    ("Paragraph", BlockType.PARAGRAPH),
]


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        for text, block_type in CASES:
            with self.subTest(text=text):
                res = block_to_block_type(text)
                expect = block_type

                message = f"Expected {expect}, got {res}"

                self.assertEqual(res, expect, message)
