from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
        
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    
    lines = block.split("\n")
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph    
        return block_type_quote
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph    
        return block_type_unordered_list
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph    
        return block_type_unordered_list
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}."):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    
    return block_type_paragraph

def markdown_to_html_node(mardown):
    blocks = markdown_to_blocks(mardown)

    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    raise ValueError("Invalid block type: " + block_type)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)

def heading_to_html_node(block):
    header_lvl = 0

    for char in block:
        if char == "#":
            header_lvl += 1
        else:
            break
    
    if header_lvl > 6:
        raise ValueError(f"Invalid heading level: {header_lvl}")
    
    text = block[header_lvl + 1 : ]
    children = text_to_children(text)

    return ParentNode(f'h{header_lvl}', children)

def code_to_html_node(block):
    children = text_to_children(block[3:-3])
    code = ParentNode('code', children)
    return ParentNode('pre', [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    quote = " ".join(new_lines)
    children = text_to_children(quote)
    return ParentNode('blockquote', children)

def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ul', html_items)

def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode('li', children))
    return ParentNode('ol', html_items)

def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        lines = block.split("\n")
        for line in lines:
            if line.startswith("# "):
                return line.lstrip("#").strip()
            
    raise ValueError("No h1 header found")