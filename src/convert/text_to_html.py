from src.nodes.types import TextType

# from src.html.node import HTMLNode

from src.nodes.html.tags import str_to_tag as tag_type
# from src.html.tags import HTMLTag

from src.nodes.html.leaf import LeafNode


def text_to_html(text_node):
    """
    Convert a TextType Enum to an HTMLTag enum
    """
    text_tag = text_node.text_type
    html_tag = text_tag

    text = text_node.text
    props = {}

    match (text_tag):
        case TextType.NORMAL:
            pass
        case TextType.LINK:
            props = {"href": text_node.url}
        case TextType.IMAGE:
            text = ""
            props = {"src": text_node.url,
                     "alt": text_node.text}

    leaf = LeafNode(html_tag.value, text, props)
    return leaf
