import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_1(self):
        html_node = HTMLNode(props={"href":"https://www.google.com"})
        props = html_node.props_to_html()
        self.assertEqual(props, ' href="https://www.google.com"')

    def test_props_2(self):
        html_node = HTMLNode(props={"href":"https://www.google.com",
                                    "target":"_blank"})
        props = html_node.props_to_html()
        self.assertEqual(props, ' href="https://www.google.com" target="_blank"')

    def test_htmlnode_values(self):
        html_node = HTMLNode("div", "Hello")
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_htmlnode_repr(self):
        html_node = HTMLNode("a", "google", None, {"href":"https://www.google.com"})
        self.assertEqual(
            html_node.__repr__(),
            "HTMLNode(a, google, children: None, {'href': 'https://www.google.com'})"
        )

    def test_leafnode_values(self):
        leaf_node = LeafNode("p", "Hello")
        self.assertEqual(leaf_node.tag, "p")
        self.assertEqual(leaf_node.value, "Hello")
        self.assertEqual(leaf_node.children, None)
        self.assertEqual(leaf_node.props, None)

    def test_leafnode_to_html(self):
        leaf_node = LeafNode("p", "This is a paragraph")
        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph</p>")

        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Click me!</a>')

        leaf_node = LeafNode(None, "This is a text")
        self.assertEqual(leaf_node.to_html(), "This is a text")

        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_leafnode_repr(self):
        leaf_node = LeafNode("a", "google", {"href":"https://www.google.com"})
        self.assertEqual(
            leaf_node.__repr__(),
            "LeafNode(a, google, {'href': 'https://www.google.com'})"
        )

    def test_parentnode_values(self):
        parent_node = ParentNode(
                        "p",
                        [
                            LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text")
                        ],
                    )
        self.assertEqual(parent_node.tag, "p")
        self.assertListEqual(parent_node.children, [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")])

    def test_parentnode_to_html(self):
        parent_node = ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        )
        
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

        parent_node = ParentNode(
                            "div",
                            [
                                ParentNode(
                                    "div",
                                    [
                                        LeafNode("p", "Paragraph"),
                                        LeafNode("b", "Bold")
                                    ]
                                    ),
                                LeafNode("a", "google", {"href":"https://www.google.com"}),
                            ],
                        )
        
        self.assertEqual(
            parent_node.to_html(),
            '<div><div><p>Paragraph</p><b>Bold</b></div><a href="https://www.google.com">google</a></div>'
        )

        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold")]).to_html()

        with self.assertRaises(ValueError):
            ParentNode("a", None).to_html()

    def test_parentnode_repr(self):
        parent_node = ParentNode(
                        "p",
                        [
                            LeafNode("a", "google", {"href":"https://www.google.com"}),
                        ],
                    )
        self.assertEqual(
            parent_node.__repr__(),
            "ParentNode(p, children: [LeafNode(a, google, {'href': 'https://www.google.com'})], None)"
        )
        

if __name__ == "__main__":
    unittest.main()