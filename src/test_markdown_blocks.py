import unittest

from markdown_blocks import markdown_to_blocks

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