from src.textnode import TextNode, TextType
from src.html.node import HTMLNode
from src.html.tags import str_to_tag as tag_type
from src.html.tags import HTMLTag

import enum as Enum


def text_to_html(text_node):
    """
    Convert a TextNode object to an HTMLNode object

    :param text_node: TextNode: The TextNode object to convert

    :return: HTMLNode: The HTMLNode object
    """
    tag = text_type_to_html_tag(text_node.text_type)
    value = text_node.text
    children = []
    props = {}

    return HTMLNode(tag=tag, value=value, children=children, props=props)


def text_type_to_html_tag(text_tag):
    """
    Convert a TextType Enum to an HTMLTag enum
    """

    match (text_tag):
        case TextType.H1:
            return HTMLTag.H1
        case TextType.H2:
            return HTMLTag.H2
        case TextType.H3:
            return HTMLTag.H3
        case TextType.H4:
            return HTMLTag.H4
        case TextType.H5:
            return HTMLTag.H5
        case TextType.H6:
            return HTMLTag.H6
        case TextType.BOLD:
            return HTMLTag.B
        case TextType.STRONG:
            return HTMLTag.STRONG
        case TextType.ITALIC:
            return HTMLTag.I
        case TextType.EM:
            return HTMLTag.EM
        case TextType.S:
            return HTMLTag.S
        case TextType.STRIKE:
            return HTMLTag.STRIKE
        case TextType.DEL:
            return HTMLTag.DEL
        case TextType.BLOCKQUOTE:
            return HTMLTag.BLOCKQUOTE
        case TextType.CODE:
            return HTMLTag.CODE
        case TextType.LINK:
            return HTMLTag.A
        case TextType.IMAGE:
            return HTMLTag.IMG
        case TextType.NORMAL:
            return HTMLTag.P
        case _:
            raise ValueError(f"Invalid text type: {text_tag}")
