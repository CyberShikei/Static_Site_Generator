from .nodes import (ParentNode,
                    LeafNode,
                    TextType,
                    TextNode,
                    BlockType
                    )
from .mardown_blocks import markdown_to_blocks
from .block_to_block_type import block_to_block_type
from .text_to_nodes import text_to_textnodes
from .text_node_to_html_node import text_node_to_html_node

import re


def md_to_html_nodes(markdown) -> ParentNode:
    """
    Converts a Markdown doc to a ParentNode.

    Args:
        markdown: The markdown doc to convert.

    Returns:
        A ParentNode representing the markdown doc.
    """

    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = None
        if block_type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            html_nodes = []
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                html_nodes.append(html_node)
            html_node = ParentNode(tag="p", children=html_nodes)
        elif __is_heading(block_type):
            text_node = __get_heading_text_node(block)
            html_node = text_node_to_html_node(text_node)
        elif block_type == BlockType.CODE:
            text_node = __code_block_to_text_node(block)
            html_node = text_node_to_html_node(text_node)
        elif block_type == BlockType.QUOTE:
            html_node = __quote_block_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            html_node = __list_block_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            html_node = __ord_list_block_to_html_node(block)
        # html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return ParentNode(tag="div", children=children)


def __ord_list_block_to_html_node(block: str) -> TextNode:
    lines = block.split('\n')
    child_nodes = []
    for line in lines:
        new_node = TextNode(re.sub(r'^\d+\. ', '', line),
                            TextType.ORDERED_LIST)
        html_node = text_node_to_html_node(new_node)
        child_nodes.append(html_node)

    parent_node = ParentNode(tag="ol", children=child_nodes)

    return parent_node


def __list_block_to_html_node(block: str) -> TextNode:
    lines = block.split('\n')
    child_nodes = []
    for line in lines:
        new_node = TextNode(re.sub(r'^\* ', '', line), TextType.UNORDERED_LIST)
        html_node = text_node_to_html_node(new_node)
        child_nodes.append(html_node)

    parent_node = ParentNode(tag="ul", children=child_nodes)

    return parent_node


def __quote_block_to_html_node(block: str) -> TextNode:
    block = re.sub(r'^> ', '', block)
    text_node = TextNode(block, TextType.QUOTE)
    html_node = text_node_to_html_node(text_node)
    return html_node


def __code_block_to_text_node(block: str) -> TextNode:
    block = re.sub(r'^```', '', block)
    block = re.sub(r'```$', '', block)

    return TextNode(block, TextType.CODE)


def __get_heading_text_node(block: str) -> TextNode:
    old_block = block
    block = __strip_heading(block)

    match block_to_block_type(old_block):
        case BlockType.H1:
            return TextNode(block, TextType.H1)
        case BlockType.H2:
            return TextNode(block, TextType.H2)
        case BlockType.H3:
            return TextNode(block, TextType.H3)
        case BlockType.H4:
            return TextNode(block, TextType.H4)
        case BlockType.H5:
            return TextNode(block, TextType.H5)
        case BlockType.H6:
            return TextNode(block, TextType.H6)
        case _:
            return None


def __strip_heading(block: str) -> str:
    return re.sub(r'^#+\s*', '', block)


def __is_heading(block_type: BlockType) -> bool:
    return block_type in (BlockType.H1,
                          BlockType.H2,
                          BlockType.H3,
                          BlockType.H4,
                          BlockType.H5,
                          BlockType.H6)
