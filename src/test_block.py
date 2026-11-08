import unittest
from block import markdown_to_blocks, block_to_block_type

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    def test_markdown_to_blocks2(self):
        md = """
    This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_block_type1(self):
        md = "### Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type.value, "heading")
    def test_block_type2(self):
        md = """```
if x == 0:
    return True
```"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type.value, "code")
    def test_block_type3(self):
        md = """>This is the start
> This is the middle
>This is the end"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type.value, "quote")
    def test_block_type4(self):
        md = """- This is the first line
- This is the next
"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type.value, "unordered_list")
    def test_block_type5(self):
        md = """1. This is the start
2. This is the middle
3. This is the end"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type.value, "ordered_list")
    def test_block_type6(self):
        md = """
This is just a normal paragraph
It's not like any of the other block types
"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type.value, "paragraph")
    def test_block_type7(self):
        md = """1. This is the start
4. This is the middle
3. This is the end"""
        block_type = block_to_block_type(md)
        self.assertNotEqual(block_type.value, "ordered_list") 