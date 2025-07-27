def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda item: item.strip(), blocks))
    blocks = list(filter(lambda item: len(item) > 0, blocks))
    return blocks

