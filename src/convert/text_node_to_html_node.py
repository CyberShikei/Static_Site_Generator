# TextNode to HTMLNode
from src.nodes import (TextNode,
                       LeafNode,
                       TextType
                       )


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """
    Convert a TextNode to an HTMLNode

    :param text_node: TextNode: The TextNode to convert

    :return: HTMLNode: The converted HTMLNode
    """
    text = text_node.text
    url = text_node.url
    text_type = text_node.text_type

    tag = text_type.value

    if text_type == TextType.IMAGE:
        html_node = LeafNode(tag=tag, value="", props={"src": url,
                                                       "alt": text})
    elif text_type == TextType.LINK:
        html_node = LeafNode(tag=tag, value=text, props={"href": url})
    else:
        html_node = LeafNode(tag=tag, value=text)

    return html_node
