#!venv/bin/python3
from static_copy import copy_files
from page_create import generate_page

STATIC_DIR = "static/"
PUBLIC_DIR = "public/"

MD_INPUT = "content/index.md"
TEMPLATE_INPUT = "template.html"
HTML_OUTPUT = "public/index.html"


def main():
    copy_files(STATIC_DIR, PUBLIC_DIR)

    generate_page(MD_INPUT, TEMPLATE_INPUT, HTML_OUTPUT)


if __name__ == "__main__":
    main()
