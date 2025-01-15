import unittest

from src.nodes.types import TextType, MDType, to_text_type, to_md_type

TEST_CASES = {
    "text": {TextType.NORMAL: "",
             TextType.TEXT: "",
             TextType.BOLD: "b",
             TextType.ITALIC: "i",
             TextType.CODE: "code",
             TextType.LINK: "a",
             TextType.IMAGE: "img",
             TextType.H1: "h1",
             TextType.H2: "h2",
             TextType.H3: "h3",
             TextType.H4: "h4",
             TextType.H5: "h5",
             TextType.H6: "h6"},
    "md": {MDType.NORMAL: "",
           MDType.TEXT: "",
           MDType.BOLD: "**",
           MDType.ITALIC: "*",
           MDType.CODE: "`",
           MDType.LINK: "[",
           MDType.IMAGE: "!",
           MDType.H1: "#",
           MDType.H2: "##",
           MDType.H3: "###",
           MDType.H4: "####",
           MDType.H5: "#####",
           MDType.H6: "######"}
}


class TestTypes(unittest.TestCase):
    def test_text_type(self):
        cases = TEST_CASES.copy()
        text_case = cases["text"][TextType.BOLD]

        self.assertEqual(text_case, "b")

    def test_text_type_eq(self):
        cases = TEST_CASES.copy()
        text_case = cases["text"][TextType.BOLD]
        text_case2 = TextType.BOLD.value

        self.assertEqual(text_case, text_case2)

    def test_md_type(self):
        cases = TEST_CASES.copy()
        md_case = cases["md"][MDType.BOLD]

        self.assertEqual(md_case, "**")

    def test_md_type_eq(self):
        cases = TEST_CASES.copy()
        md_case = cases["md"][MDType.BOLD]
        md_case2 = MDType.BOLD.value

        self.assertEqual(md_case, md_case2)

    def test_text_type_to_md_type(self):
        text_case = TextType.BOLD
        md_case = MDType.BOLD

        converted = to_text_type(md_case)

        self.assertEqual(converted, text_case)

    def test_md_type_to_text_type(self):
        md_case = MDType.BOLD
        text_case = TextType.BOLD

        converted = to_md_type(text_case)

        self.assertEqual(converted, md_case)

    def test_all_to_text_type(self):
        pass
