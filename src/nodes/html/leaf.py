# LeafNode class inherits from HTMLNode
#
# The LeafNode class inherits from the HTMLNode class and represents a
#           leaf HTML element, i.e., an element that cannot have children.
#   It has the following attributes:
#     - tag: a string that represents the HTML tag
#     - value: a string that represents the value of the HTML element
#     - props: a dictionary that represents the properties of the HTML element
#
from .node import HTMLNode


class LeafNode(HTMLNode):

    def __init__(self,
                 tag="",
                 # Value is required for LeafNode
                 value="",
                 props={}):
        super().__init__(tag=tag,
                         value=value,
                         children=[],
                         props=props)

    def to_html(self):
        TAG = self.tag
        return f'<{TAG}{self.props_to_html()}>{self.value}</{TAG}>'

    def __eq__(self, other):
        is_tag = self.tag == other.tag
        is_value = self.value == other.value
        is_props = self.props == other.props

        return is_tag and is_value and is_props

    def __repr__(self):
        rep_tag = self.tag
        rep_val = self.value
        rep_props = self.props

        rep_string = f"""LeafNode(
        tag={rep_tag},
        value={rep_val},
        props={rep_props}
)"""

        return rep_string

    # override the setter for children
    @property
    def children(self):
        return None

    @children.setter
    def children(self, value):
        raise ValueError("LeafNode cannot have children")
