from enum import Enum


class TextType(Enum):
    NORMAL = ""
    TEXT = NORMAL
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"


class MDType(Enum):
    NORMAL = ""
    TEXT = ""
    BOLD = "**"
    ITALIC = "*"
    CODE = "`"
    LINK = "["
    IMAGE = "!"
    H1 = "#"
    H2 = "##"
    H3 = "###"
    H4 = "####"
    H5 = "#####"
    H6 = "######"


def to_text_type(md_in):
    md_type = md_in

    if isinstance(md_type, str):
        md_type = _type_str_to_md(md_type)
    elif not isinstance(md_type, MDType):
        raise ValueError("Invalid type")

    return _match_md(md_type)


def to_md_type(text_in):
    text_type = text_in

    if isinstance(text_type, str):
        text_type = _type_str_to_text(text_type)
    elif not isinstance(text_type, TextType):
        raise ValueError("Invalid type")

    return _match_text(text_type)


def _match_md(md_tyoe):
    match (md_tyoe):
        case MDType.NORMAL:
            return TextType.NORMAL
        case MDType.TEXT:
            return TextType.TEXT
        case MDType.BOLD:
            return TextType.BOLD
        case MDType.ITALIC:
            return TextType.ITALIC
        case MDType.CODE:
            return TextType.CODE
        case MDType.LINK:
            return TextType.LINK
        case MDType.IMAGE:
            return TextType.IMAGE
        case MDType.H1:
            return TextType.H1
        case MDType.H2:
            return TextType.H2
        case MDType.H3:
            return TextType.H3
        case MDType.H4:
            return TextType.H4
        case MDType.H5:
            return TextType.H5
        case MDType.H6:
            return TextType.H6
        case _:
            return None


def _match_text(text_type):
    match (text_type):
        case TextType.NORMAL:
            return MDType.NORMAL
        case TextType.TEXT:
            return MDType.TEXT
        case TextType.BOLD:
            return MDType.BOLD
        case TextType.ITALIC:
            return MDType.ITALIC
        case TextType.CODE:
            return MDType.CODE
        case TextType.LINK:
            return MDType.LINK
        case TextType.IMAGE:
            return MDType.IMAGE
        case TextType.H1:
            return MDType.H1
        case TextType.H2:
            return MDType.H2
        case TextType.H3:
            return MDType.H3
        case TextType.H4:
            return MDType.H4
        case TextType.H5:
            return MDType.H5
        case TextType.H6:
            return MDType.H6
        case _:
            return None


def _type_str_to_text(string):
    for text_type in TextType:
        if text_type.value == string:
            return text_type

    return None


def _type_str_to_md(string):
    for md_type in MDType:
        if md_type.value == string:
            return md_type

    return None
