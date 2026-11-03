import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_html_1(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, None)
    def test_prop_html_2(self):
        props = {"href": "https://www.google.com"}
        node = HTMLNode(None, None, None, props)
        result = node.props_to_html()
        self.assertEqual(result, " href=\"https://www.google.com\"")
    def test_prop_html_3(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(None, None, None, props)
        result = node.props_to_html()
        self.assertEqual(result, " href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()