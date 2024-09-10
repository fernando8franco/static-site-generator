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

if __name__ == "__main__":
    unittest.main()