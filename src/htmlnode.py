class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ""
        if self.props:
            for prop, value in self.props.items():
                string += f' {prop}="{value}"'
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {str(self.props)}, {self.props_to_html()})"
