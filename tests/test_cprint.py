import io

from coloring import cprint
from coloring.consts import *


def test_cprint_no_args():
    f = io.StringIO()
    cprint(file=f)
    s = f.getvalue()
    assert s == f"\n"


def test_cprint_red_color():
    text = "Hello"
    f = io.StringIO()
    cprint(text, c="red", file=f)
    s = f.getvalue()
    assert s == f"{CSI}38;2;255;0;0m{text}{RESET_COLOR}\n"


def test_cprint_styles():
    text = "Hello"
    # bold
    f = io.StringIO()
    cprint(text, s="b", file=f)
    s = f.getvalue()
    assert s == f"{BOLD}{text}{RESET_BOLD_AND_DIM}\n"

    # underline
    f = io.StringIO()
    cprint(text, s="u", file=f)
    s = f.getvalue()
    assert s == f"{UNDERLINE}{text}{RESET_UNDERLINE}\n"

    # cross
    f = io.StringIO()
    cprint(text, s="c", file=f)
    s = f.getvalue()
    assert s == f"{CROSS}{text}{RESET_CROSS}\n"


def test_cprint_flush_signture():
    text = "Hello"
    # bold
    f = io.StringIO()
    cprint(text, s="b", file=f, flush=True)
    s = f.getvalue()
    assert s == f"{BOLD}{text}{RESET_BOLD_AND_DIM}\n"
