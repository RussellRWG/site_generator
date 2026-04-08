import unittest

from text_functions import extract_markdown_images, extract_markdown_links


class TestTextFunctions(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

        matches = extract_markdown_images(
            "This is text does have an image"
        )
        self.assertListEqual([], matches)

        matches = extract_markdown_images(
            "This text has two images! ![image](https://i.imgur.com/zjjcJKZ.png) ![image2](https://i.imgur.com/zjjcJK343Z.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://i.imgur.com/zjjcJK343Z.png")], matches)
        return

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
        return



if __name__ == "__main__":
    unittest.main()
