from typing import List

from src.nodes.types import BlockType

import re


def markdown_to_blocks(markdown) -> List[str]:
    lines = markdown.split("\n")

    blocks = []

    curr_blck_type = BlockType.PARAGRAPH

    for line in lines:
        line_type = match_line(line)

        if curr_blck_type != BlockType.CODE and curr_blck_type != BlockType.QUOTE:
            if line_type != BlockType.CODE and line_type != BlockType.QUOTE:
                if line_type != BlockType.PARAGRAPH:
                    line = line.lstrip()
                    blocks.append((line, line_type))
                    curr_blck_type = line_type
                elif line_type == BlockType.PARAGRAPH:
                    blocks.append((line, line_type))
                    curr_blck_type = line_type
            elif line_type != BlockType.PARAGRAPH:
                line = line.lstrip()
                blocks.append((line, line_type))
                curr_blck_type = line_type
            else:
                blocks.append((line, line_type))
                curr_blck_type = line_type
        else:
            blocks.append((line, curr_blck_type))

        if line.endswith("```") or line.endswith(">"):
            curr_blck_type = BlockType.PARAGRAPH

    return blocks


def match_line(line: str) -> BlockType:
    if line.startswith("#"):
        return get_header_level(line)
    elif line.startswith("*") or line.startswith("-"):
        return BlockType.UNORDERED_LIST
    elif check_ordered_list(line):
        return BlockType.ORDERED_LIST
    elif line.startswith("```") or code_block_has_spaces_before(line):
        return BlockType.CODE
    elif line.startswith(">") or quote_block_has_spaces_before(line):
        return BlockType.QUOTE
    else:
        return BlockType.PARAGRAPH

    # return BlockType.PARAGRAPH


def code_block_has_spaces_before(line: str) -> bool:
    re_pattern = r"\s*```"

    return re.match(re_pattern, line) is not None


def quote_block_has_spaces_before(line: str) -> bool:
    re_pattern = r"\s*>"

    return re.match(re_pattern, line) is not None


def check_open(block_type: BlockType) -> bool:
    return block_type in [BlockType.CODE, BlockType.QUOTE]


def get_header_level(header: str) -> int:
    lvl = header.count("#")
    result = BlockType.H1

    if lvl >= 6:
        result = BlockType.H6
    elif lvl == 5:
        result = BlockType.H5
    elif lvl == 4:
        result = BlockType.H4
    elif lvl == 3:
        result = BlockType.H3
    elif lvl == 2:
        result = BlockType.H2

    return result


def check_ordered_list(line: str) -> bool:
    return re.match(r"\d+\.", line) is not None
