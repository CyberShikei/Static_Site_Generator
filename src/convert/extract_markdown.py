import re

from typing import List, Tuple

IMG_PATTERN = r"!\[([^\]]+)\]\(([^\)]+)\)"
LINK_PATTERN = r"\[([^\]]+)\]\(([^\)]+)\)"

# EXAMPLE USSAGE
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_image(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


def extract_images(markdown: str) -> List[Tuple[str, str]]:
    """
    Extracts image alt text and URLs from a string.

    Args:
        text (str): The input text containing markdown-style images.

    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple is (alt text, URL).
    """
    # Regular expression to match Markdown-style images
    image_pattern = IMG_PATTERN
    text = markdown

    result = []
    cursor = 0

    # Iterate over all matches
    for match in re.finditer(image_pattern, text):
        start, end = match.span()
        alt_text, image_url = match.groups()

        # Add text before the image as a plain text fragment
        if cursor < start:
            result.append((text[cursor:start], None))

        # Add the alt text and URL
        result.append((alt_text, image_url))

        # Move the cursor forward
        cursor = end

    # Add any remaining text after the last image
    if cursor < len(text):
        result.append((text[cursor:], None))

    return result


def extract_links(markdown: str) -> List[Tuple[str, str]]:
    """
    Extracts text fragments and links from a string.

    Args:
        text (str): The input text containing markdown-style links.

    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple is (text, link).
                               The `link` will be None for plain text fragments.
    """
    # Regular expression to match Markdown-style links
    link_pattern = LINK_PATTERN
    text = markdown

    result = []
    cursor = 0

    # Iterate over all matches
    for match in re.finditer(link_pattern, text):
        start, end = match.span()
        link_text, link_url = match.groups()

        # Add text before the link as a plain text fragment
        if cursor < start:
            result.append((text[cursor:start], None))

        # Add the link text and URL
        result.append((link_text, link_url))

        # Move the cursor forward
        cursor = end

    # Add any remaining text after the last link
    if cursor < len(text):
        result.append((text[cursor:], None))

    return result
