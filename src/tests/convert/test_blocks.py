import unittest

from src.convert.mardown_blocks import markdown_to_blocks
from src.nodes.types import BlockType


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading
This is a paragraph of text. It has some **bold** and *italic* words inside of it.
* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected = [
            ("# This is a heading", BlockType.H1),
            ("This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
             BlockType.PARAGRAPH),
            ("* This is the first list item in a list block", BlockType.UNORDERED_LIST),
            ("* This is a list item", BlockType.UNORDERED_LIST),
            ("* This is another list item", BlockType.UNORDERED_LIST)
        ]
        result = markdown_to_blocks(markdown)

        err_msg = f"""Expected {expected},

        but got {result}"""

        self.assertEqual(result, expected, err_msg)

    def test_ordered_list(self):
        markdown = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""

        expected = [
            ("1. This is the first list item in a list block", BlockType.ORDERED_LIST),
            ("2. This is a list item", BlockType.ORDERED_LIST),
            ("3. This is another list item", BlockType.ORDERED_LIST)
        ]
        result = markdown_to_blocks(markdown)

        err_msg = f"""Expected {expected},

        but got {result}"""

        self.assertEqual(result, expected, err_msg)

    def test_code_block(self):
        markdown = """## Some Python code
        ```python
def hello_world():
    print("Hello, World!")
```"""

        expected = [
            ("## Some Python code", BlockType.H2),
            ("```python", BlockType.CODE),
            ("def hello_world():", BlockType.CODE),
            ("    print(\"Hello, World!\")", BlockType.CODE),
            ("```", BlockType.CODE)
        ]
        result = markdown_to_blocks(markdown)

        err_msg = f"""Expected {expected},

        but got {result}"""

        self.assertEqual(result, expected, err_msg)


if __name__ == '__main__':
    unittest.main()
