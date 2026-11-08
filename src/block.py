from enum import Enum
import re

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
    elif re.findall(r"^(>\s{0,1}.*(\n|$))+(?<!\n)$", block) != []:
        return BlockType.QUOTE
    elif re.findall(r"^(?:-\s.*(?:\r?\n|$))+(?<!\n)$", block) != []:
        return BlockType.UNORDERED_LIST
    elif re.findall(r"^(?:[1-9][0-9]{0,5}\.\s.*(?:\r?\n|$))+$", block) != []:
        # Checks if the list is numbered properly
        lines = block.splitlines("\n")
        numbered_order = list(map(str, range(1, len(lines)+1)))
        actual_order = [line.strip().split()[0][0] for line in lines]
        if actual_order == numbered_order:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

    
    