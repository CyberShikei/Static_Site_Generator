#!venv/bin/python3
from static_copy import copy_files
from page_create import generate_pages_recursive

STATIC_DIR = "static/"
PUBLIC_DIR = "public/"

MD_INPUT = "content/"
TEMPLATE_INPUT = "template.html"
HTML_OUTPUT = "public/"


def main():
    copy_files(STATIC_DIR, PUBLIC_DIR)

    generate_pages_recursive(MD_INPUT, TEMPLATE_INPUT, PUBLIC_DIR)


if __name__ == "__main__":
    main()
