import unittest

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter
from textnode import TextNode

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]
        )

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(matches,
                            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
                            )
        
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches,
                            [("to boot dev", "https://www.boot.dev"), 
                            ("to youtube", "https://www.youtube.com/@bootdotdev")]
                            )
        
    def test_extract_markdown_images_and_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches,
                            [("to boot dev", "https://www.boot.dev")]
                            )
        matches = extract_markdown_images(text)
        self.assertListEqual(matches,
                            [("to youtube", "https://www.youtube.com/@bootdotdev")]
                            )