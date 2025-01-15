import re

from typing import List

from src.convert.split_markdown import split_nodes_image, split_nodes_link
from src.convert.md_to_text import split_nodes_delimiter
from src.nodes.text import TextNode
from src.nodes.types import TextType


BOLD_PATTERN = r"\*\*(.*?)\*\*"
ITALIC_PATTERN = r"\*(.*?)\*"
CODE_PATTERN = r"`(.*?)`"


def text_to_textnodes(text: str) -> List[TextNode]:
    """
    Converts a string to a list of TextNodes.

    Args:
        text (str): The input text to convert.

    Returns:
        List[TextNode]: A list of TextNodes.
    """
    nodes = [TextNode(text, TextType.NORMAL)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = bold_nodes(nodes)
    nodes = italic_nodes(nodes)
    nodes = code_nodes(nodes)

    return nodes


def bold_nodes(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = split_nodes_delimiter(old_nodes, "**")
    return new_nodes


def italic_nodes(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = split_nodes_delimiter(old_nodes, "*")
    return new_nodes


def code_nodes(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes = split_nodes_delimiter(old_nodes, "`")
    return new_nodes
