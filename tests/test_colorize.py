import pytest
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


def test_hex_colors():
    text = "Hello world"

    colorized_text = colorize(text, c="#000000")
    assert colorized_text == colorize(text, c=(0, 0, 0))

    colorized_text = colorize(text, c="#FFFFFF")
    assert colorized_text == colorize(text, c=(255, 255, 255))

    colorized_text = colorize(text, c="#ffffff")
    assert colorized_text == colorize(text, c=(255, 255, 255))

    colorized_text = colorize(text, c="#FfFfFf")
    assert colorized_text == colorize(text, c=(255, 255, 255))

    colorized_text = colorize(text, c="#512e5f")
    assert colorized_text == colorize(text, c=(81, 46, 95))

    colorized_text = colorize(text, c="#512E5f")
    assert colorized_text == colorize(text, c=(81, 46, 95))


def test_hex_color_exception():
    text = "Hello world"

    # less then 7 characters
    with pytest.raises(ValueError):
        colorize(text, c="#512E5")

    # adding non hexadecimal character
    with pytest.raises(ValueError):
        colorize(text, c="#512o5")

    # more then 7 characters
    with pytest.raises(ValueError):
        colorize(text, c="#512E5ff")

    # more then 7 characters
    with pytest.raises(ValueError):
        colorize(text, c="#512E5fea")

    # less the 7 characters
    with pytest.raises(ValueError):
        colorize(text, c="#512E")
