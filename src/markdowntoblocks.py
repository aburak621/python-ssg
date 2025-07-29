from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda item: item.strip(), blocks))
    blocks = list(filter(lambda item: len(item) > 0, blocks))
    return blocks


def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")
    is_quote_block = True
    for line in lines:
        if line.startswith(">"):
            continue
        is_quote_block = False
        break
    if is_quote_block:
        return BlockType.QUOTE

    is_ul_block = True
    for line in lines:
        if line.startswith("- "):
            continue
        is_ul_block = False
        break
    if is_ul_block:
        return BlockType.UL

    is_ol_block = True
    for i, line in enumerate(lines):
        if line.startswith(str(i + 1) + ". "):
            continue
        is_ol_block = False
        break
    if is_ol_block:
        return BlockType.OL

    return BlockType.PARAGRAPH
