# convert markdown to text blocks

from typing import List

from .types import BlockType


class Block:
    def __init__(self, text: str, block_type: BlockType):
        self.text = text
        self.block_type = block_type
