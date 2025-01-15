import re

from typing import List

from src.nodes.types import to_text_type, to_md_type

from src.nodes.text import TextNode
from src.nodes.types import TextType

# patterns for bold, italic, and code text
# dont remove the pattern before or after the string when split
BOLD_PATTERN = r"\*\*(.*?)\*\*"
ITALIC_PATTERN = r"\*(.*?)\*"
CODE_PATTERN = r"`(.*?)`"


def split_nodes_delimiter(old_nodes, delimiter) -> List[TextNode]:
    # NEW IMPLEMENTATION
    new_nodes = []
    delim_type = match_delim(delimiter)

    for node in old_nodes:
        if node.text_type == TextType.NORMAL:
            parts = split_node(node, delim_type)
            # clean empty parts
            parts = [part for part in parts if part.text]
            new_nodes.extend(parts)
        else:
            new_nodes.append(node)

    return new_nodes


def split_node(node: TextNode, delim_type: TextType) -> List[TextNode]:
    if delim_type == TextType.BOLD:
        return split_bold_text(node.text)
    elif delim_type == TextType.ITALIC:
        return split_italic_text(node.text)
    elif delim_type == TextType.CODE:
        return split_code_text(node.text)
    else:
        return node


def match_delim(delim: str) -> TextType:
    match delim:
        case "**":
            return TextType.BOLD
        case "*":
            return TextType.ITALIC
        case "`":
            return TextType.CODE
        case _:
            return TextType.NORMAL


def split_bold_text(text: str) -> List[TextNode]:
    pattern = BOLD_PATTERN

    # This will store the resulting parts
    result = []
    last_pos = 0

    # Use finditer to iterate over all matches
    for match in re.finditer(pattern, text):
        # Add the text before the match
        result.append(TextNode(text[last_pos:match.start()], TextType.NORMAL))
        # Add the match itself
        result.append(TextNode(match.group(1), TextType.BOLD))
        # Update the last position
        last_pos = match.end()

    # Add the text after the last match
    result.append(TextNode(text[last_pos:], TextType.NORMAL))

    return result


def split_italic_text(text: str) -> List[TextNode]:
    pattern = ITALIC_PATTERN

    # This will store the resulting parts
    result = []
    last_pos = 0

    # Use finditer to iterate over all matches
    for match in re.finditer(pattern, text):
        # Add the text before the match
        result.append(TextNode(text[last_pos:match.start()], TextType.NORMAL))
        # Add the match itself
        result.append(TextNode(match.group(1), TextType.ITALIC))
        # Update the last position
        last_pos = match.end()

    # Add the text after the last match
    result.append(TextNode(text[last_pos:], TextType.NORMAL))

    return result


def split_code_text(text: str) -> List[TextNode]:
    pattern = CODE_PATTERN

    # This will store the resulting parts
    result = []
    last_pos = 0

    # Use finditer to iterate over all matches
    for match in re.finditer(pattern, text):
        # Add the text before the match
        result.append(TextNode(text[last_pos:match.start()], TextType.NORMAL))
        # Add the match itself
        result.append(TextNode(match.group(1), TextType.CODE))
        # Update the last position
        last_pos = match.end()

    # Add the text after the last match
    result.append(TextNode(text[last_pos:], TextType.NORMAL))

    return result
