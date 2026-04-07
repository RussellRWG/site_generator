from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super(ParentNode, self).__init__(tag=tag, children=children, props=props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag must have a value")
        if self.children == None:
            raise ValueError("ParentNode must have Children")
        children_html = ''.join(map(lambda x: x.to_html(), self.children))
        html = f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        return html
