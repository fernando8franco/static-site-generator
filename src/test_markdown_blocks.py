import unittest

from markdown_blocks import block_to_block_type, extract_title, markdown_to_blocks, markdown_to_html_node

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        blocks = markdown_to_blocks(
            """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        )
        self.assertListEqual(blocks,
                             ['# This is a heading', 
                              'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                              '* This is the first list item in a list block\n* This is a list item\n* This is another list item'])
        
        blocks = markdown_to_blocks(
            """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is another list item                          """
        )
        self.assertListEqual(blocks,
                             ['# This is a heading', 
                              'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                              '* This is another list item'])
        
    def test_block_to_block_type(self):
        block_type = block_to_block_type("paragraph")
        self.assertEqual(block_type, "paragraph")

        block_type = block_to_block_type("# heading")
        self.assertEqual(block_type, "heading")
        block_type = block_to_block_type("### heading")
        self.assertEqual(block_type, "heading")
        block_type = block_to_block_type("###### heading")
        self.assertEqual(block_type, "heading")

        block_type = block_to_block_type("```code\ncode```")
        self.assertEqual(block_type, "code")

        block_type = block_to_block_type(">quote\n>quote")
        self.assertEqual(block_type, "quote")

        block_type = block_to_block_type("* unordered_list\n* unordered_list")
        self.assertEqual(block_type, "unordered_list")
        block_type = block_to_block_type("- unordered_list\n- unordered_list")
        self.assertEqual(block_type, "unordered_list")

        block_type = block_to_block_type("* unordered_list\n* unordered_list")
        self.assertEqual(block_type, "unordered_list")
        block_type = block_to_block_type("1. ordered_list\n2. ordered_list\n3. ordered_list")
        self.assertEqual(block_type, "ordered_list")

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_code(self):
        md = """
```This is code
java
python```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is code\njava\npython</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_extract_title(self):
        markdown = """
# Header 1
"""
        header = extract_title(markdown)
        self.assertEqual(header, "Header 1")