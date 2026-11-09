from enum import Enum
import re
from htmlnode import *
from textnode import *

def markdown_to_blocks(markdown):
    lines: list[str] = markdown.split("\n\n")
    lines[:] = [line.strip() for line in lines]
    cleaned_lines = []
    for line in lines:
        if line != "":
            cleaned_lines.append(line)
    return cleaned_lines

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING ="heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.findall(r"^\#{1,6}\s.+$", block) != []:
        return BlockType.HEADING
    elif re.findall(r"^\`{3}\n(.+\n)+?\`{3}$", block) != []:
        return BlockType.CODE
    elif re.findall(r"^(>\s{0,1}.+(\n|$))+(?<!\n)$", block) != []:
        return BlockType.QUOTE
    elif re.findall(r"^(?:-\s.+(?:\r?\n|$))+(?<!\n)$", block) != []:
        return BlockType.UNORDERED_LIST
    elif re.findall(r"^(?:[1-9][0-9]{0,5}\.\s.+(?:\r?\n|$))+(?<!\n)$", block) != []:
        # Checks if the list is numbered properly
        lines = block.splitlines("\n")
        numbered_order = list(map(str, range(1, len(lines)+1)))
        actual_order = [line.strip().split()[0][0] for line in lines]
        if actual_order == numbered_order:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        htmlnode = None
        block_type = block_to_block_type(block)
        
        if block_type.value == "heading":
            split_head = block.split(" ", 1)
            head = split_head[0]
            text = split_head[1]
            children = text_to_children(text)
            htmlnode = ParentNode(f"h{len(head)}", children)

        elif block_type.value == "code":
            code_text = block[4:-3]
            text_node = TextNode(code_text, TextType.TEXT)
            code_node = text_node_to_html_node(text_node)
            code_parent = ParentNode("code", [code_node])
            htmlnode = ParentNode("pre", [code_parent])
        
        elif block_type.value == "quote":
            items = block.split("\n")
            lines = []
            for item in items:
                item_text = ""
                if item[1] == " ":
                    item_text = item[2:]
                else:
                    item_text = item[1:]
                lines.append(item_text)
            full_text = " ".join(lines)
            children = text_to_children(full_text)
            htmlnode = ParentNode("blockquote", children)
        
        elif block_type.value == "unordered_list":
            items = block.split("\n")
            item_nodes = []
            for item in items:
                item_text = item[2:]
                item_children = text_to_children(item_text)
                item_node = ParentNode("li", item_children)
                item_nodes.append(item_node)
            htmlnode = ParentNode("ul", item_nodes)
        
        elif block_type.value == "ordered_list":
            items = block.split("\n")
            item_nodes = []
            for item in items:
                digit = 1
                while item[digit] != ".":
                    digit += 1
                item_text = item[digit+2:]
                item_children = text_to_children(item_text)
                item_node = ParentNode("li", item_children)
                item_nodes.append(item_node)
            htmlnode = ParentNode("ol", item_nodes)
        
        else:
            edited_text = " ".join(block.split("\n"))
            children = text_to_children(edited_text)
            htmlnode = ParentNode("p", children)
        
        nodes.append(htmlnode)
    return ParentNode("div", nodes)
        


def text_to_children(text):
    first_node = TextNode(text, TextType.TEXT)
    nodes = []
    nodes = split_nodes_delimiter([first_node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

    