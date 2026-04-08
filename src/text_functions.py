import re

image_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def extract_markdown_images(text):
    images = image_pattern.findall(text)
    return images

def extract_markdown_links(text):
    links = link_pattern.findall(text)
    return links
