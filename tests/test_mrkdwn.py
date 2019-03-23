import unittest
import pgdocs.mrkdwn as md


class TestMarkdown(unittest.TestCase):
    def test_h1(self):
        self.assertEqual(md.h1("hi", False), "# hi")
        self.assertEqual(md.h1("hi"), "# hi\n")

    def test_h2(self):
        self.assertEqual(md.h2("hi", False), "## hi")
        self.assertEqual(md.h2("hi"), "## hi\n")


if __name__ == "__main__":
    unittest.main()
