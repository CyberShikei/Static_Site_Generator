# convert markdown to text blocks

from src.nodes import TextType


class Block:
    def __init__(self, text: str, block_type: TextType):
        self.text = text
        self.block_type = block_type

    def __repr__(self):
        return f"Block({self.text}, {self.block_type})"
