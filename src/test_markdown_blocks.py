import unittest

from markdown_blocks import block_to_block_type, markdown_to_blocks

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