import unittest

from src.convert import markdown_to_blocks


class TestMdToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = """   # This is a heading

This is  Paragraph line

* This is a list item
* This is another list item"""

        blocks = markdown_to_blocks(markdown)

        expected = [
            ["# This is a heading"],
            "This is  Paragraph line",
            ["* This is a list item", "* This is another list item"],
        ]

        message = f"___GOT {blocks}"

        self.assertEqual(blocks, expected, message)

    def test_markdown_to_blocks_2(self):
        markdown = """
        ```python
        TestCodeBlock
        awadawdawd
        ```
        
        # a HEADING"""

        blocks = markdown_to_blocks(markdown)

        expected = [
            [
                "```python",
                "        TestCodeBlock",
                "        awadawdawd",
                "```",
            ],
            ["# a HEADING"],
        ]

        message = f"___GOT {blocks}"

        print(message)

        self.assertEqual(blocks, expected, message)
