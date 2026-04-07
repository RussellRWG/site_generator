from enum import Enum
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None, alt_text=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt_text = alt_text


    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, props = {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src":self.url, "alt":self.alt_text})
