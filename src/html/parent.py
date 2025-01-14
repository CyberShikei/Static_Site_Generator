from .node import HTMLNode
from .leaf import LeafNode


class ParentNode(HTMLNode):
    # tag and children are required for ParentNode
    # does not take a value
    def __init__(self,
                 tag="",
                 children=[],
                 props={}):

        # self._enforce_required(tag, children)

        super().__init__(tag=tag,
                         value="",
                         children=children,
                         props=props)

    def __eq__(self, other):
        is_tag = self.tag == other.tag
        is_children = self.children == other.children
        is_props = self.props == other.props

        return is_tag and is_children and is_props

    def __repr__(self):
        rep_tag = self.tag
        rep_children = self.children
        rep_props = self.props

        rep_string = f"""ParentNode(
        tag={rep_tag},
        children={rep_children},
        props={rep_props}
)"""

        return rep_string

    def to_html(self):
        self._enforce_required(self.tag, self.children)

        line = f'<{self.tag}'
        line += f'{self.props_to_html()}>'
        for child in self.children:
            line += f'{child.to_html()}'
        line += f'</{self.tag}>'

        result = line

        return result

    def _enforce_required(self, tag, children):
        ParentNode._no_tag(tag)
        ParentNode._no_children(children)

    def _has_tag(tag):
        return tag != ""

    def _has_children(children):
        return children != []

    def _no_tag(tag):
        if not ParentNode._has_tag(tag):
            _err = "Tag is required for ParentNode"
            raise ValueError(_err)

    def _no_children(children):
        if not ParentNode._has_children(children):
            _err = "Children are required for ParentNode"
            raise ValueError(_err)
