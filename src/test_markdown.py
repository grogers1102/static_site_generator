import unittest
from block import markdown_to_html_node

class TestMarkdown(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_headingblock(self):
        md = """
# Heading 1

#### **Heading** 4
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h4><b>Heading</b> 4</h4></div>"
        )
    def test_quoteblock(self):
        md = """
> This is regular text.
> This is _italic_ text.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is regular text. This is <i>italic</i> text.</blockquote></div>"
        )
    def test_unorderedblock(self):
        md = """
- First: `code text`
- Second: **bold text**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First: <code>code text</code></li><li>Second: <b>bold text</b></li></ul></div>"
        ) 
    def test_orderedblock(self):
        md = """
1. The next line has an image.
2. ![image](https://i.imgur.com/zjjcJKZ.png)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>The next line has an image.</li><li><img src=\"https://i.imgur.com/zjjcJKZ.png\" alt=\"image\"></li></ol></div>"
        ) 
    def test_combination(self):
        md = """
# Heading 1

```
This is text that _should_ remain
the **same** even with inline stuff
```

- First: `code text`
- Second: **bold text**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            ("<div><h1>Heading 1</h1><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre><ul><li>First: <code>code text</code></li><li>Second: <b>bold text</b></li></ul></div>")
        ) 
if __name__ == "__main__":
    unittest.main()