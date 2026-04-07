import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Link</a>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Header 1")
        self.assertEqual(node.to_html(), "<h1>Header 1</h1>")

if __name__ == "__main__":
    unittest.main()
