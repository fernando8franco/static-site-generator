import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        html_node = HTMLNode(props={"href":"https://www.google.com"})
        props = html_node.props_to_html()
        self.assertEqual(props, ' href="https://www.google.com"')

if __name__ == "__main__":
    unittest.main()