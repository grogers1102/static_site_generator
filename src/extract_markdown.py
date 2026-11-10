import re

def extract_markdown_images(text) -> list[tuple[str, str]]:
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_title(markdown):
    if markdown[0] != "#":
        raise Exception("Error: No header detected.")
    title = markdown.split(" ", 1)[1].split("\n", 1)[0].strip()
    return title

