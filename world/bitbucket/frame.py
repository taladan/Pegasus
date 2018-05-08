#!/usr/bin/python
# -*- coding: utf-8 -*-

from evennia.utils import justify, to_str


__author__ = "Jamie Crosby <taladan@gmail.com>"
__version__ = "Alpha"
__license__ = "[GLPv3](https://www.gnu.org/licenses/gpl-3.0.en.html)"

class Frame(object):
    """outter frame constructor

    my_frame = Frame(align="l",
                     indent=0,
                     pad_width=0,
                     pad_char=" "
                     text="My string",
                     frame_type="body",
                     width=79):

    Alignment:

        align=X

        X must be one of:
            - "l" -> left justify
            - "r" -> right justify
            - "c" -> center justify
            - "f" -> full justify
            - None -> no justify

        Defaults to None

    Default Border Characters:

        no_default_chars=False

        Uses spaces instead of characters for all your borders:

        Defaults to False

        The border characters are settable on the frame object:

            bottom_border_char: border_char of the outter frame - default: "═"
            bottom_left_corner: bottom left corner of the outter frame - default: "╚"
            bottom_right_corner bottom right corner of the outter frame - default: "╝"
            left_border_char: Character for the left border of the outter frame - default: "║"
            left_tee: Character for the left tee of the frame - default: "╠"
            right_border_char: Character for the left border of the frame - default: "║"
            right_tee: Character for the right tee of the frame - default: "╣"
            top_border_char: border_char of the outter frame - default: "═"
            top_left_corner: Character for the top left corner of the outter frame - default: "╔"
            top_right_corner: Character for the top right corner of the outter frame - default: "╗"

    Indention:

        indent=N

        N is a positive int that indents lines, however paragraphs are retained.

    Pad Width:

        pad_width=N

        N is a positive int spacing inside the frame around any type of insert (text/inner frames).

    Pad Character:

        pad_char="X"

        X is a single ascii or unicode character to fill the pad of a frame.


    Text:

        text="string" where string is the text that you want to be displayed in the frame.

        The Frame will justify and indent the text but retain paragraphs.

    Type of frame:

        frame_type=X

       X must be one of:

            - "header" -> uses left and right TEE characters on bottom corners
            - "body" -> uses left and right TEE characters on bottom corners
            - "footer" -> uses corner characters on bottom corners

       Defaults to "body".

    Width:
        width=N

        The width of the frame (N) must be a positive int greater than or equal to 3.

        Defaults to 79

    """

    def __init__(self, text="", align="l", indent=0, pad_char=" ", pad_width=0,
                 frame_type="body",
                 wipe_default_chars=False, width=79):
        super(Frame, self).__init__()

        # Localize input
        self.align = align
        self.frametype = frame_type
        self.indent = indent
        self.pad_char = pad_char
        self.pad_width = pad_width
        self.text = text
        self.width = width
        self.bottom_border_character = "═"
        self.bottom_left_corner = "╚"
        self.bottom_right_corner = "╝"
        self.corners = 2
        self.left_tee = "╠"
        self.right_tee = "╣"
        self.left_border_char = "║"
        self._padding = self.pad_char * self.pad_width
        self.left_border = self.left_border_char + self._padding
        self._padded_width = self.width - self.pad_width
        self.right_border_char = "║"
        self.right_border = self._padding + self.right_border_char
        self._text_width = self.text_width()
        self.top_border_character = "═"
        self.top_left_corner = "╔"
        self.top_right_corner = "╗"

        border_chars = [
            self.bottom_border_character,
            self.bottom_left_corner,
            self.bottom_right_corner,
            self.left_border_char,
            self.left_tee,
            self.right_border_char,
            self.right_tee,
            self.top_border_character,
            self.top_left_corner,
            self.top_right_corner,
        ]

        # Reset header characters if user indicates no_default_chars
        space = " "
        if wipe_default_chars == True:
            for i, attr in enumerate(border_chars):
                border_chars[i] = space

        # parse the text
        self.parsed = self.parser(text)

        # Set up borders

        self.border = Border(frametype=self.frametype,
                             bottom_border_character=border_chars[0],
                             bottom_left_corner=border_chars[1],
                             bottom_right_corner=border_chars[2],
                             left_border_character=border_chars[3],
                             left_tee=border_chars[4],
                             right_border_character=border_chars[5],
                             right_tee=border_chars[6],
                             top_border_character=border_chars[7],
                             top_left_corner=border_chars[8],
                             top_right_corner=border_chars[9],
                             width=self.width
                             )

    def text_width(self):
        """:return: the text width of the frame"""
        return self.width - self.corners - self.pad_width * 2 - self.indent

    def parser(self, text):
        """parse text to width, alignment and indentation for packing

        :returns: Parsed string
        """
        if self.align == None:
            parsed = text
        else:
            parsed = justify(text, width=self._text_width, align=self.align,
                             indent=self.indent)
        return parsed

    def frame(self):
        """create a frame and populate it

        Valid frame types are:
        header, body, footer

        :returns: Frame object
        """
        # parse text first

        border = self.border
        # wrap the borders around the text
        first = self.border.top
        body = self.pack_line(self.parsed)
        last = border.bottom

        # Top border is first, then the body, bottom border is last
        frame_tuple = (first, body, last)
        return "\n".join(frame_tuple)

    def test(self):
        text = "The quick brown fox jumped over the lazy dog.  Four score and seven years ago " \
               "our forefathers brought unto this land a new nation.  The man in black fled " \
               "across the desert and the gunslinger followed, though not too closely behind " \
               "because he got held up in tull.  What a bitch, that alice."

        my_frame = Frame(text, width=50, align="c", indent=1, pad_width=1, pad_char='.').frame()
        print(my_frame)

class Inner(Frame):
    """inner frame constructor

    my_inner_frame = Frame(align="l",
                           indent=0,
                           pad_width=0,
                           pad_char=" "
                           text="My string",
                           frame_type="body",
                           width=79):

    Alignment:

        align=X

        X must be one of:
            - "l" -> left justify
            - "r" -> right justify
            - "c" -> center justify
            - "f" -> full justify
            - None -> no justify

        Defaults to None

    Default Border Characters:

        no_default_chars=False

        Uses spaces instead of characters for all your borders:

        Defaults to False

        The border characters are settable on the frame object:

            bottom_border: Bottom border character of the inner frame - default: "─"
            bottom_left_corner: Bottom left corner of the inner frame - default: "╰"
            bottom_right_corner: Bottom right corner of the inner frame - default: "╯"
            left_border: Left border character of the inner frame - default: "│"
            left_tee: Left tee character of the inner frame - default: "├"
            right_border: Right border character of the inner frame - default: "│"
            right_tee: Right tee character of the inner frame - default: "┤"
            top_border: Top border character of the inner frame - default: "─"
            top_left_corner: Top left corner of the inner frame - default: "╭"
            top_right_corner: top right corner of the inner frame -  default: "╮"

    Indention:

        indent=N

        N is a positive int that indents lines, however paragraphs are retained.

    Pad Width:

        pad_width=N

        N is a positive int spacing inside the frame around any type of insert (text/inner frames).

    Pad Character:

        pad_char="X"

        X is a single ascii or unicode character to fill the pad of a frame.

    Root frame:

        root=Frame_Object

        The root frame must be set to a valid Frame object for inner frames to populate.

    Text:

        text="string" where string is the text that you want to be displayed in the frame.

        The Frame will justify and indent the text but retain paragraphs.

    Type of frame:

        frame_type=X

       X must be one of:

            - "header" -> uses left and right TEE characters on bottom corners
            - "body" -> uses left and right TEE characters on bottom corners
            - "footer" -> uses corner characters on bottom corners

       Defaults to "body".

    Width:
        width=N

        The width of the frame (N) must be a positive int greater than or equal to 3 but less
        than the padded outter frame.

        Defaults to Outter Frame Width - Outter Padding

    """

    def __init__(self, root=None, *args, **kwargs):
        super(Inner, self).__init__()

        none_root_error = \
            "Inner frames must have a valid root frame of type {0}".format(type(Frame))

        if root == None:
            raise ValueError(none_root_error)
        else:
            self.bottom_border_character = "─"
            self.bottom_left_corner = "╰"
            self.bottom_right_corner = "╯"
            self.left_border_char = "│"
            self.left_border = self.left_border + pad + self.left_border_char
            self.left_tee = "├"
            self.right_border_char= "│"
            self.right_border = pad + self.right_border_char + self.right_border
            self.right_tee = "┤"
            self._text_width = lambda: self.text_width()
            self.top_border_character = "─"
            self.top_left_corner = "╭"
            self.top_right_corner = "╮"
            self.use_header = False
            self.width = self._padded_width


class Border(object):
    """supplies border paramemters

    :param: bottom: bottom border
    :param: top: top border
    :param: right: right border character
    :param: left: left border character
    """
    def __init__(self, bottom_border_character=None, bottom_left_corner=None,
                 bottom_right_corner=None, frametype=None, left_border_character=None,
                 left_tee=None, right_border_character=None, right_tee=None,
                 top_border_character=None, top_left_corner=None, top_right_corner=None,
                 width=None,
                 ):
        self.bottom_border_character = bottom_border_character
        self.bottom_left_corner = bottom_left_corner
        self.bottom_right_corner = bottom_right_corner
        self.frametype = frametype
        self.left_border_character = left_border_character
        self.left_tee = left_tee
        self.right_border_character = right_border_character
        self.right_tee = right_tee
        self.top_border_character = top_border_character
        self.top_left_corner = top_left_corner
        self.top_right_corner = top_right_corner
        self.width = width

        _bbc = bottom_border_character
        _blc = bottom_left_corner
        _brc = bottom_right_corner
        _frametype = frametype
        _lbc = left_border_character
        _lt = left_tee
        _rbc = right_border_character
        _rt = right_tee
        _tbc = top_border_character
        _tlc = top_left_corner
        _trc = top_right_corner

        attrdict = {
            "Frametype": frametype,
            "bottom_border_character": _bbc,
            "bottom_left_corner": _blc,
            "bottom_right_corner": _brc,
            "frametype": _frametype,
            "left_border_character": _lbc,
            "left_tee": _lt,
            "right_border_character": _rbc,
            "right_tee": _rt,
            "top_border_character": _tbc,
            "top_left_corner": _tlc,
            "top_right_corner": _trc,
        }

        len = width - 2

        # Errors
        valid_types = "header", "body", "footer"
        wrong_frame_type_error = "A frame must be one of type: {0}".format(repr(valid_types))

        if _frametype is not None and _frametype.lower() not in valid_types:
            raise ValueError(wrong_frame_type_error)
        elif _frametype is not None:
            _frametype = _frametype.lower()

        # Build inlays between corners
        top_inlay = _tbc * len
        bottom_inlay = _bbc * len

        # Borders

        self.left = _lbc
        self.right = _rbc

        print()

        # borders can have a corner or tee on the corners
        if _frametype in "header":
            self.top = _tlc + top_inlay + _trc
            self.bottom = _lt + bottom_inlay + _rt
        elif _frametype in "body":
            self.top = _lt + bottom_inlay + _rt
            self.bottom = _lt + bottom_inlay + _rt
        elif _frametype in "footer":
            self.bottom = _blc + bottom_inlay + _brc

    def pack_line(self, lines):
        """packs a line with borders

        :return: Frame line"""
        ag = []
        pad =
        for line in lines.split("\n"):
            ag.append(self.left_border_char
                      + pad
                      + line
                      + pad
                      + self.right_border_char)
        return '\n'.join(ag)


