import unittest
from extract_markdown import extract_markdown_links, extract_markdown_images

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images1(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_images2(self):
        matches = extract_markdown_images(
            "This is text with ![image](https://i.imgur.com/zjjcJKZ.png) and ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("rick roll", "https://i.imgur.com/aKaOqIh.gif")], matches) 
    def test_extract_markdown_links1(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
    def test_extract_markdown_links2(self):
        matches = extract_markdown_links(
            "This is text with links [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")], matches) 
    def test_extract_markdown_links3(self):
        matches = extract_markdown_links(
            "This is text with an image ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)
