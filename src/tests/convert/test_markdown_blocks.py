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
            "# This is a heading",
            "This is  Paragraph line",
            "* This is a list item\n* This is another list item",
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
            "```python\n        TestCodeBlock\n        awadawdawd\n```",
            "# a HEADING",
        ]

        message = f"___GOT {blocks}"

        print(message)

        self.assertEqual(blocks, expected, message)

    def test_markdown_to_blocks_various_inputs(self):
        markdown = """ # This is a heading

This is  Paragraph line


* This is a list item
* This is another list item

```python

TestCodeBlock

awadawdawd

```

> This is a blockquote
> This is another blockquote

1. This is a numbered list item
2. This is another numbered list item"""

        blocks = markdown_to_blocks(markdown)

        expected = [
            "# This is a heading",
            "This is  Paragraph line",
            "* This is a list item\n* This is another list item",
            "```python\n\nTestCodeBlock\n\nawadawdawd\n\n```",
            "> This is a blockquote\n> This is another blockquote",
            "1. This is a numbered list item\n2. This is another numbered list item"
        ]

        message = f"___GOT {blocks}"

        self.assertEqual(blocks, expected, message)

    def test_markdown_to_blocks_trailing_spaces(self):
        markdown = """ # This is a heading

This is  Paragraph line     

* This is a list item
* This is another list item  
"""

        blocks = markdown_to_blocks(markdown)

        expected = [
            "# This is a heading",
            "This is  Paragraph line",
            "* This is a list item\n* This is another list item",
        ]

        message = f"___GOT {blocks}"

        self.assertEqual(blocks, expected, message)
