from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: TextNode):
        if (self.text == other.text and self.text_type == other.text_type
        and self.url == other.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case text_node.text_type.TEXT:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b", text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i", text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code", text_node.text)
        case text_node.text_type.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case text_node.text_type.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Text type not valid")

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, 
text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if not node.text_type.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception("Markdown Syntax Error: No closing delimiter detected")
            for x in range(0, len(split_text)):
                if split_text[x] == "":
                    continue
                if x % 2 != 0:
                    new_nodes.append(TextNode(split_text[x], text_type))
                else:
                    new_nodes.append(TextNode(split_text[x], TextType.TEXT))
    return new_nodes
            
                
            
    

