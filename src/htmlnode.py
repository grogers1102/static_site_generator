class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return None
        result = ""
        for prop in self.props:
            result += f" {prop}=\"{self.props[prop]}\""
        return result
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value is None")
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html() if self.props != None else ""}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is None")
        elif not self.children:
            raise ValueError("Children is None")
        else:
            child_output = f""
            for child in self.children:
                child_output += child.to_html()
            return f"<{self.tag}{self.props_to_html() if self.props != None else ""}>{child_output}</{self.tag}>"