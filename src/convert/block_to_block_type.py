from typing import List

from .nodes import BlockType

import re


def block_to_block_type(md_block):
    if not isinstance(md_block, str):
        raise ValueError("Invalid type")

    # text untill first space
    leading_string = md_block.split(" ")[0]

    if md_block[0] == "#":
        head_level = __match_heading_level(leading_string)
        if head_level:
            return head_level

    # first 3 characters of the line
    starts_with = leading_string[:3]

    # if code
    if starts_with == "```":
        if md_block.endswith("```"):
            return BlockType.CODE

    # if ordered list (any number followed by a dot then followd by a space)
    if re.match(r"\d+\.", leading_string):
        return BlockType.ORDERED_LIST

    match leading_string:
        case "-":
            return BlockType.UNORDERED_LIST
        case "*":
            return BlockType.UNORDERED_LIST
        case ">":
            return BlockType.QUOTE
        case _:
            return BlockType.PARAGRAPH


def __get_heading_level(md_block):
    return md_block.count("#")


def __match_heading_level(leading_string):
    match leading_string:
        case "#":
            return BlockType.H1
        case "##":
            return BlockType.H2
        case "###":
            return BlockType.H3
        case "####":
            return BlockType.H4
        case "#####":
            return BlockType.H5
        case "######":
            return BlockType.H6
        case _:
            return 0
