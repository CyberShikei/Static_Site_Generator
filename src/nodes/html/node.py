# Description: HTMLNode class
#
# The HTMLNode class is a base class that represents an HTML element.
#   It has the following attributes:
#     - tag: a string that represents the HTML tag
#     - value: a string that represents the value of the HTML element
#     - children: a list of HTMLNode objects that represent the children of
#               the HTML element
#     - props: a dictionary that represents the properties of the HTML element

from .tags import HTMLTag, str_to_tag

# HTMLNode class


class HTMLNode():
    _tag: str
    _value: str
    _children: list
    _props: dict

    def __init__(self,
                 tag="",
                 value="",
                 # list of children HTMLNode objects
                 children=[],
                 props={}
                 ):
        self._tag = tag
        self._value = value
        self._children = children
        self._props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f'{key}="{value}" '

        # remove trailing space
        result = result[:-1]

        return result

    def __eq__(self, other):
        is_tag = self.tag == other.tag
        is_value = self.value == other.value
        is_props = self.props == other.props
        is_children = self.children == other.children

        return is_tag and is_value and is_props and is_children

    def __repr__(self):
        rep_tag = self.tag
        rep_val = self.value
        rep_props = self.props
        rep_children = self.children

        rep_string = f"""HTMLNode(
        tag={rep_tag},
        value={rep_val},
        props={rep_props},
        children={rep_children}
)"""

        return rep_string

    # setter and getter for tag
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    # setter and getter for value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    # setter and getter for children
    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value

    # setter and getter for props
    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, value):
        self._props = value
