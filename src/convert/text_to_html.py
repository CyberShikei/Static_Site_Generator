from src.nodes.types import TextType

# from src.html.node import HTMLNode

from src.html.tags import str_to_tag as tag_type
# from src.html.tags import HTMLTag

from src.html.leaf import LeafNode


def text_to_html(text_node):
    """
    Convert a TextType Enum to an HTMLTag enum
    """
    text_tag = text_node.text_type
    html_tag = tag_type(text_tag.value)

    text = text_node.text
    props = {}

    match (text_tag):
        case TextType.LINK:
            props = {"href": text_node.url}
        case TextType.IMAGE:
            text = ""
            props = {"src": text_node.url,
                     "alt": text_node.text}

    leaf = LeafNode(html_tag, text, props)
    return leaf
