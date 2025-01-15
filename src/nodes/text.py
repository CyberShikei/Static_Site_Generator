from .types import TextType


class TextNode:
    _text = ""
    _url = None
    _text_type = None

    def __init__(self,
                 text,
                 text_type,
                 url=None
                 ):
        """
        Create a new TextNode object

        :param text: str: The text content of the node
        :param text_type: str: The type of text content
        :param url: str: The URL if the text is a link

        :raises ValueError: If text_type is not a valid TextType
                (case-insensitive)

        :return: None
        """
        self._text = text
        self._url = url
        self._text_type = self._enforece_type(text_type)

    def __eq__(self, other):
        is_text = self.text == other.text
        is_type = self.text_type == other.text_type
        is_url = self.url == other.url

        return is_text and is_type and is_url

    def __repr__(self):
        s_txt = self.text
        s_typ = self.text_type
        s_url = self.url
        s_text = f"TextNode({s_txt}, {s_typ}, {s_url})"

        return s_text

    def _enforece_type(self, text_type):
        if isinstance(text_type, TextType):
            return text_type

        upper_text = text_type
        # check if text_type is valid string for TextType Enum
        if upper_text not in TextType.__members__:
            raise ValueError(f"""Invalid text type: {text_type}
            Valid types are: {TextType.__members__.keys()}""")

        # return as TextType Enum
        return TextType[upper_text]

    # setter for text_type
    @property
    def text_type(self):
        return self._text_type

    @property
    def text(self):
        return self._text

    @property
    def url(self):
        return self._url
