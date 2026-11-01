from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: "TextType", url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: "TextNode"):
        if (self.text == other.text and self.text_type == other.text_type
        and self.url == other.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
