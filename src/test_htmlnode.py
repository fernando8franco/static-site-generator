import unittest

from htmlnode import HTMLNode

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

    def test_values(self):
        html_node = HTMLNode("div", "Hello")
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_repr(self):
        html_node = HTMLNode("a", "google", None, {"href":"https://www.google.com"})
        self.assertEqual(
            html_node.__repr__(),
            "HTMLNode(a, google, children: None, {'href': 'https://www.google.com'})"
        )

if __name__ == "__main__":
    unittest.main()