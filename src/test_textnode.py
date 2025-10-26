import unittest
from textnode import TextNode, TextType, LeafNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_text_becomes_raw_leaf(self):
        tn = TextNode("hello", TextType.TEXT)
        ln = text_node_to_html_node(tn)
        self.assertIsInstance(ln, LeafNode)
        self.assertIsNone(ln.tag)           # raw text (no tag)
        self.assertEqual(ln.value, "hello")
        self.assertIsNone(ln.props)



if __name__ == "__main__":
    unittest.main()