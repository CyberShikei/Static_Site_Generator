import re


def extract_image(markdown: str) -> str:
    return re.findall(r"!\[.*\]\((.*)\)", markdown)


def extract_link(markdown: str) -> str:
    return re.findall(r"\[.*\]\((.*)\)", markdown)


def extract_code(markdown: str) -> str:
    return re.findall(r"```(.*)```", markdown)


def extract_markdown(markdown: str) -> dict:
    return {
        "image": extract_image(markdown),
        "link": extract_link(markdown),
        "code": extract_code(markdown)
    }
