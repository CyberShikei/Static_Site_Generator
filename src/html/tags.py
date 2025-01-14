from enum import Enum

# HTML tags


class HTMLTag(Enum):
    # HTML tags with matching markdown syntax
    # https://www.markdownguide.org/basic-syntax/
    # https://www.w3schools.com/tags/

    # Headings
    H1 = "H1"
    H2 = "H2"
    H3 = "H3"
    H4 = "H4"
    H5 = "H5"
    H6 = "H6"

    # Paragraph
    P = "P"

    # Bold
    B = "B"
    STRONG = "STRONG"

    # Italic
    I = "I"
    EM = "EM"

    # Strikethrough
    S = "S"
    STRIKE = "STRIKE"
    DEL = "DEL"

    # Blockquote
    BLOCKQUOTE = "BLOCKQUOTE"

    # Code
    CODE = "CODE"

    # Link
    A = "A"

    # Image
    IMG = "IMG"

    # span
    SPAN = "SPAN"

    # div
    DIV = "DIV"

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

    # if tag == "":
    #     return tag

    upper_tag = tag.upper()
    # check if tag is valid string for HTMLTag Enum
    if upper_tag not in HTMLTag.__members__:
        raise ValueError(f"""Invalid tag: {tag}
        Valid tags are: {HTMLTag.__members__.keys()}""")

    # return as HTMLTag Enum
    return HTMLTag(upper_tag)
