from htmlnode import HTMLNode
from typing import ValuesView

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("LeafNode value cannot be None")
        super(LeafNode, self).__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag == None:
            return self.value
        else:
            prop_str = self.props_to_html()
            return f"<{self.tag}{prop_str}>{self.value}</{self.tag}>"
