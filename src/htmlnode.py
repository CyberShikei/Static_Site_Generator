class HTMLNode():
    def __init__(self,
                 tag="",
                 value="",
                 # list of children HTMLNode objects
                 children=[],
                 props={}
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'

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
