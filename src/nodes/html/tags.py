from enum import Enum

from src.nodes.types import BlockType
# HTML tags


class HTMLTag(Enum):
    # HTML tags with matching markdown syntax
    # https://www.markdownguide.org/basic-syntax/
    # https://www.w3schools.com/tags/

    # Headings
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"

    # Paragraph
    P = "p"

    # Bold
    B = "b"

    # Italic
    ITALIC = "i"

    # Code
    CODE = "code"

    # Link
    A = "a"

    # Image
    IMG = "img"

    NORMAL = ""

    def __str__(self):
        return self.value


def str_to_tag(tag):
    """
    Convert a string to an HTMLTag Enum

    :param tag: str: The string to convert to an HTMLTag Enum

    :raises ValueError: If tag is not a valid HTMLTag

    :return: HTMLTag: The HTMLTag Enum
    """
    if isinstance(tag, HTMLTag):
        return tag

    if isinstance(tag, BlockType):
        return mardown_block_tag_to_html_tag(tag)
    # if tag == "":
    #     return tag

    upper_tag = tag
    # check if tag is valid string in HTMLTag Enum values
    if not is_in_enum(tag, HTMLTag):
        valid_tags = [e.value for e in HTMLTag]
        raise ValueError(f"""Invalid HTML tag: {tag}
        Valid tags: {valid_tags}""")

    return HTMLTag(upper_tag)


def mardown_block_tag_to_html_tag(block_type):
    """
    Convert a BlockType string to an HTMLTag enum
    """
    if block_type == BlockType.H1:
        return HTMLTag.H1
    elif block_type == BlockType.H2:
        return HTMLTag.H2
    elif block_type == BlockType.H3:
        return HTMLTag.H3
    elif block_type == BlockType.H4:
        return HTMLTag.H4
    elif block_type == BlockType.H5:
        return HTMLTag.H5
    elif block_type == BlockType.H6:
        return HTMLTag.H6
    elif block_type == BlockType.PARAGRAPH:
        return HTMLTag.P
    elif block_type == BlockType.CODE:
        return HTMLTag.CODE
    elif block_type == BlockType.QUOTE:
        return HTMLTag.BLOCKQUOTE
    elif block_type == BlockType.UNORDERED_LIST:
        return HTMLTag.UL
    elif block_type == BlockType.ORDERED_LIST:
        return HTMLTag.OL
    else:
        raise ValueError("Invalid block type")


def is_in_enum(value, enum):
    return value in [e.value for e in enum]
