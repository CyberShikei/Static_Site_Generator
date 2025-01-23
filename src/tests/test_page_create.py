import unittest

from src.page_create import extract_title


class TestTitleExtract(unittest.TestCase):
    def test_title_extract(self):
        markdown = "# My Title\n\nSome content"
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")

    def test_title_extract_no_title(self):
        markdown = "Some content"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_title_extract_empty_title(self):
        markdown = "# \n\nSome content"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_title_extract_late_heading(self):
        markdown = "Some content\n# My Title"
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")
