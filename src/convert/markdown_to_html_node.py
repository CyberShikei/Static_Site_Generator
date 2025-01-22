from src.nodes import ParentNode, LeafNode, TextType, TextNode

from .mardown_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type


def md_to_html_node(markdown) -> ParentNode:
    """
    Converts a Markdown doc to a ParentNode.

    Args:
        markdown: The markdown doc to convert.

    Returns:
        A ParentNode representing the markdown doc.
    """

    blocks = markdown_to_blocks(markdown)
    root = ParentNode()

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == TextType.NORMAL:
