import io

from coloring import rgbprint
from coloring.consts import *


def test_rgbprint_red_color():
    text = "Hello"
    f = io.StringIO()
    rgbprint(255, 0, 0, text, file=f)
    s = f.getvalue()
    assert s == f"{CSI}38;2;255;0;0m{text}{RESET_COLOR}\n"


def test_rgbprint_bold():
    text = "Hello"
    f = io.StringIO()
    rgbprint(255, 0, 0, text, s="b", file=f)
    s = f.getvalue()
    assert s == f"{CSI}38;2;255;0;0m{BOLD}{text}{RESET_BOLD_AND_DIM}{RESET_COLOR}\n"
