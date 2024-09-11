import unittest

from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_texnode_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_eq_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)
        
    def test_textnode_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node = TextNode("text", "text")
        self.assertEqual(text_node_to_html_node(node), LeafNode(None, "text"))
        node = TextNode("text", "bold")
        self.assertEqual(text_node_to_html_node(node), LeafNode("b", "text"))
        node = TextNode("text", "italic")
        self.assertEqual(text_node_to_html_node(node), LeafNode("i", "text"))
        node = TextNode("text", "code")
        self.assertEqual(text_node_to_html_node(node), LeafNode("code", "text"))
        node = TextNode("text", "link", "google.com")
        self.assertEqual(text_node_to_html_node(node), LeafNode("a", "text", {"href": "google.com"}))
        node = TextNode("text", "image", "google.com")
        self.assertEqual(text_node_to_html_node(node), LeafNode("img", "", {"src": "google.com", "alt": "text"}))

        with self.assertRaises(ValueError):
            node = TextNode("text", "no_type")
            text_node_to_html_node(node), LeafNode(None, "text")


if __name__ == "__main__":
    unittest.main()