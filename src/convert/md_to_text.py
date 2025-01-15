from src.nodes.types import to_text_type, to_md_type

from src.nodes.text import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    md_delim_type = to_md_type(text_type)
    delim_type = to_text_type(md_delim_type)

    for node in old_nodes:
        if node.text_type == delim_type:
            new_nodes.append(TextNode("", text_type))
        else:
            new_nodes.append(node)

    return new_nodes
