from enum import Enum

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

    # if tag == "":
    #     return tag

    upper_tag = tag
    # check if tag is valid string in HTMLTag Enum values
    if not is_in_enum(tag, HTMLTag):
        valid_tags = [e.value for e in HTMLTag]
        raise ValueError(f"""Invalid HTML tag: {tag}
        Valid tags: {valid_tags}""")

    return HTMLTag(upper_tag)


def is_in_enum(value, enum):
    return value in [e.value for e in enum]
