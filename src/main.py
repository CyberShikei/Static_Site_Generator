#!venv/bin/python3
from textnode import TextNode


def main():
    TEXT = "Hello, World!"
    TEXT_TYPE = 'normal'
    URL = "https://www.google.com"

    node_args = (TEXT, TEXT_TYPE, URL)

    print(TextNode(*node_args))


if __name__ == "__main__":
    main()
