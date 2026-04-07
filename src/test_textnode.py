import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        bold_node = TextNode("default text", TextType.BOLD)
        italic_node = TextNode("default text", TextType.ITALIC)
        self.assertNotEqual(bold_node, italic_node)

        url_node = TextNode("has a url", TextType.TEXT, "whitehouse.gov")
        url_node2 = TextNode("has a url", TextType.TEXT, "whitehouse.gov")
        self.assertEqual(url_node, url_node2)

        url_node3 = TextNode("has a url", TextType.BOLD, "whitehouse.gov")
        url_node4 = TextNode("has a url", TextType.ITALIC, "whitehouse.gov")
        self.assertNotEqual(url_node3, url_node4)

    def test_split_node(self):
        node1 = TextNode("This is a _text_ node", TextType.TEXT)
        node2 = TextNode(
            "The second _text with a space_  second _set of_ text ", TextType.TEXT
        )
        node_list = [node1, node2]
        new_nodes = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 8)

    def test_to_html_node(self):
        def test_text(self):
            node = TextNode("This is a text node", TextType.TEXT)
            html_node = node.text_node_to_html_node()
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
