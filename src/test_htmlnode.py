import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_with_props(self):
        node = HTMLNode("div", props={"id": "main", "class": "container"})
        self.assertEqual(node.props_to_html(), ' id="main" class="container"')

    def test_props_to_html_no_props(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")

    def test_repr_output(self):
        node = HTMLNode("span", value="Hello", children=None, props={"style": "color:red"})
        expected = (
            "tag: span\nvalue: Hello\nchildren: None\nprops: {'style': 'color:red'}"
        )
        self.assertEqual(repr(node), expected)

    def test_tag_assignment(self):
        node = HTMLNode("p")
        self.assertEqual(node.tag, "p")

    def test_value_and_children(self):
        child = HTMLNode("span", value="child")
        node = HTMLNode("div", value="parent", children=[child])
        self.assertEqual(node.value, "parent")
        self.assertEqual(node.children[0].value, "child")

if __name__ == "__main__":
    unittest.main()
