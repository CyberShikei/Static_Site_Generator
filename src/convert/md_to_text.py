from src.textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delim_type = TextType.get_type_from_delimiter(delimiter)

    for node in old_nodes:
        if node.text_type == delim_type:
            new_nodes.append(TextNode("", text_type))
        else:
            new_nodes.append(node)

    return new_nodes
