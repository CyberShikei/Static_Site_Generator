from src.textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delim_type = get_type_from_delimiter(delimiter)

    for node in old_nodes:
        if node.text_type == delim_type:
            new_nodes.append(TextNode("", text_type))
        else:
            new_nodes.append(node)

    return new_nodes


def get_type_from_delimiter(delimiter):
    if delimiter == "":
        return TextType.NORMAL
    if delimiter == "**":
        return TextType.BOLD
    if delimiter == "*":
        return TextType.ITALIC
    if delimiter == "`":
        return TextType.CODE
    if delimiter == "[":
        return TextType.LINK
    if delimiter == "!":
        return TextType.IMAGE
    if delimiter == "#":
        return TextType.H1
    if delimiter == "##":
        return TextType.H2
    if delimiter == "###":
        return TextType.H3
    if delimiter == "####":
        return TextType.H4
    if delimiter == "#####":
        return TextType.H5
    if delimiter == "######":
        return TextType.H6
