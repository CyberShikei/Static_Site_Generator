from typing import List

import re


# EXAMPLE:

# INPUT:
# # This is a heading
#
# This is a paragraph of text. It has some **bold** and *italic* words inside of it.
#
# * This is the first list item in a list block
# * This is a list item
# * This is another list item

# OUTPUT:
# [
# "# This is a heading",
# "This is a paragraph of text. It has some **bold** and *italic* words inside of it,
# ["* This is the first list item in a list block,
# "* This is a list item,
# "* This is another list item,
# ],
# ]

def markdown_to_blocks(markdown: str) -> List[str]:
    lines = markdown.split("\n")

    # if code block add each line utill code block is closed,
    # same for list blocks
    # else if line is not empty add it to the blocks list

    blocks = []
    current_block = []
    current_leader = ""

    for line in lines:
        stripped_line = __strip_lead_tail_space(line)
        leader = __get_line_leader(line)

        if leader != "```" and current_leader == "```":
            current_block.append(line)
            continue
        elif leader == "```" and current_leader == "```":
            current_block.append(stripped_line)
            blocks.append(current_block)
            current_block = []
            current_leader = ""
            continue
        else:
            line = stripped_line

        if leader:
            if leader == current_leader:
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(current_block)
                current_block = [line]
                current_leader = leader
        else:
            if current_block:
                blocks.append(current_block)
                current_block = []
                current_leader = ""
            if line:
                blocks.append(line)

    if current_block:
        blocks.append(current_block)

    blocks = [__join_blocks(block) for block in blocks]

    return blocks


def __join_blocks(block: List[str]) -> str:
    if isinstance(block, str):
        return block
    return "\n".join(block)

# Leaders = [
#     "#",
#     "##",
#     "###",
#     "####",
#     "#####",
#     "######",
#     "-",
#     "*",
#     "{number}."
#     ">",
#     "```",
# ]
# LEADERS CAN HAVE SPACES BEFORE THEM


def __get_line_leader(line: str) -> str:
    line = __strip_lead_tail_space(line)
    if line.startswith("#"):
        return "#"
    if line.startswith("-"):
        return "-"
    if line.startswith("*"):
        return "*"
    if re.match(r"^\d+\.", line):
        return "{number}."
    if line.startswith(">"):
        return ">"
    if line.startswith("```"):
        return "```"
    return ""


def __strip_lead_tail_space(line: str) -> str:
    return re.sub(r"^\s+|\s+$", "", line)
