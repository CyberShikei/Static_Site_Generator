from src.nodes.text import TextNode
from src.nodes.types import TextType

from .extract_markdown import extract_links, extract_images

from typing import List

import re

# EXAMPLE:
# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]


def split_nodes_image(nodes: List[TextNode]) -> List[TextNode]:
    result = []

    for node in nodes:
        if node.text_type == TextType.NORMAL:  # Only process NORMAL nodes
            parts_and_images = extract_images(
                node.text)  # Extract images and parts
            for part, image in parts_and_images:
                if image:
                    # Append image alt text as an IMAGE node
                    result.append(TextNode(part, TextType.IMAGE, image))
                else:
                    # Append plain text as a NORMAL node
                    result.append(TextNode(part, TextType.NORMAL))
        else:
            # Non-NORMAL nodes are appended as is
            result.append(node)

    return result


def split_nodes_link(nodes: List[TextNode]) -> List[TextNode]:
    result = []

    for node in nodes:
        if node.text_type == TextType.NORMAL:  # Only process NORMAL nodes
            parts_and_links = extract_links(
                node.text)  # Extract links and parts
            for part, link in parts_and_links:
                if link:
                    # Append link text as a LINK node
                    result.append(TextNode(part, TextType.LINK, link))
                else:
                    # Append plain text as a NORMAL node
                    result.append(TextNode(part, TextType.NORMAL))
        else:
            # Non-NORMAL nodes are appended as is
            result.append(node)

    return result
