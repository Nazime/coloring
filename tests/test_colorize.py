from coloring import colorize, create_color
from coloring.consts import *


def test_colorize_rgb_color():
    text = "Hello"
    colored_text = colorize(text, c=(120, 160, 200))
    assert colored_text == f"{CSI}38;2;120;160;200m{text}{RESET_COLOR}"

    colored_text = colorize(text, c=(128, 128, 128))
    assert colored_text == f"{CSI}38;2;128;128;128m{text}{RESET_COLOR}"


def test_colorize_bold():
    text = "Hello"
    colored_text = colorize(text, c=(120, 160, 200), s="b")
    assert (
        colored_text
        == f"{CSI}38;2;120;160;200m{BOLD}{text}{RESET_BOLD_AND_DIM}{RESET_COLOR}"
    )


def test_colorize_underline():
    text = "Hello"
    colored_text = colorize(text, c=(120, 160, 200), s="u")
    assert (
        colored_text
        == f"{CSI}38;2;120;160;200m{UNDERLINE}{text}{RESET_UNDERLINE}{RESET_COLOR}"
    )


def test_colorize_style_only():
    text = "Hello"
    colored_text = colorize(text, s="u")
    assert colored_text == f"{UNDERLINE}{text}{RESET_UNDERLINE}"


def test_colorize_background():
    text = "Hello"
    colored_text = colorize(text, bg=(120, 160, 200))
    assert colored_text == f"{CSI}48;2;120;160;200m{text}{RESET_BACKGROUND}"

    colored_text = colorize(text, bg=(128, 128, 128))
    assert colored_text == f"{CSI}48;2;128;128;128m{text}{RESET_BACKGROUND}"
