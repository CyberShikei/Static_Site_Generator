from .mardown_blocks import markdown_to_blocks

from .text_to_nodes import text_to_textnodes
from .text_to_html import text_to_html

from src.nodes.types import BlockType

from src.nodes.html.node import HTMLNode
from src.nodes.html.leaf import LeafNode
from src.nodes.html.parent import ParentNode
from src.nodes.html.tags import str_to_tag


def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    blocks = join_code_blocks(blocks)

    html_nodes = []

    for block in blocks:
        if block[1] == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block[0])
            for text_node in text_nodes:
                html_node = text_to_html(text_node)
                html_nodes.append(html_node)
        elif block[1] == BlockType.CODE:
            code_node = LeafNode(str_to_tag("code"), block[0])
            html_nodes.append(code_node)
        elif block[1] == BlockType.QUOTE:
            quote_node = ParentNode(str_to_tag("blockquote"))
            html_nodes.append(quote_node)
        elif block[1] == BlockType.UNORDERED_LIST:
            ul_node = ParentNode(str_to_tag("ul"))
            html_nodes.append(ul_node)
        elif block[1] == BlockType.ORDERED_LIST:
            ol_node = ParentNode(str_to_tag("ol"))
            html_nodes.append(ol_node)
        elif block[1] in [BlockType.H1, BlockType.H2, BlockType.H3, BlockType.H4, BlockType.H5, BlockType.H6]:
            header_node = LeafNode(str_to_tag(block[1]), block[0])
            html_nodes.append(header_node)
        else:
            raise ValueError("Invalid block type")

    return html_nodes


def remove_code_block_delimiters(block):
    return block[3:-3]


def join_code_blocks(blocks):

    new_blocks = []

    in_code_block = False
    code_block = []

    for block in blocks:
        if block[1] == BlockType.CODE:
            code_block.append(block[0])

            in_code_block = True
        elif in_code_block:
            code_block = "\n".join(code_block)
            new_blocks.append(
                (remove_code_block_delimiters(code_block), BlockType.CODE))
            in_code_block = False
            code_block = []
        else:
            new_blocks.append(block)

    if in_code_block:
        code_block = "\n".join(code_block)
        new_blocks.append(
            (remove_code_block_delimiters(code_block), BlockType.CODE))

    return new_blocks
