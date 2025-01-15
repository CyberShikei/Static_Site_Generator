import unittest

from src.convert.extract_markdown import extract_image, extract_link


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_image(self):
        test_string = "![image](https://example.com/image.png)"
        expected = ["https://example.com/image.png"]

        test_result = extract_image(test_string)

        self.assertEqual(test_result, expected)

    def test_extract_image_no_image(self):
        test_string = "This is a test string"
        expected = []

        test_result = extract_image(test_string)

        self.assertEqual(test_result, expected)

    def test_extract_link(self):
        test_string = "[link](https://example.com)"
        expected = ["https://example.com"]

        test_result = extract_link(test_string)

        self.assertEqual(test_result, expected)

    def test_extract_link_no_link(self):
        test_string = "This is a test string"
        expected = []

        test_result = extract_link(test_string)

        self.assertEqual(test_result, expected)
