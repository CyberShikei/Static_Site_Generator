import unittest

from src.convert.extract_markdown import extract_images, extract_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_image(self):
        test_input = "This is text with an ![image](https://www.boot.dev/image.png) and ![another](https://www.youtube.com/@bootdotdev)"
        expected_output = [
            ("This is text with an ", None),
            ("image", "https://www.boot.dev/image.png"),
            (" and ", None),
            ("another", "https://www.youtube.com/@bootdotdev"),
        ]

        result = extract_images(test_input)

    def test_extract_links(self):
        test_input = "This is text with a [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_output = [
            ("This is text with a ", None),
            ("to boot dev", "https://www.boot.dev"),
            (" and ", None),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]

        result = extract_links(test_input)

        self.assertEqual(
            result,
            expected_output,
            msg=f"Expected {expected_output}, but got {result}",
        )
