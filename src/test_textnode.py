import unittest

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


if __name__ == "__main__":
    unittest.main()
