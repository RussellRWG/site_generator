
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def props_to_html(self):
        html = ""
        if self.props == None:
            return html
        for prop in self.props:
            html += f" {prop}=\"{self.props[prop]}\""
        return html

    def __repr__(self):
        output = f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
        return output
