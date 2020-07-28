import pytest
from coloring import create_color
from coloring.consts import *


def test_create_color():
    text = "Hello"

    mycolor = create_color(120, 160, 200)
    colored_text = mycolor(text)
    assert colored_text == f"{CSI}38;2;120;160;200m{text}{RESET_COLOR}"

    mycolor = create_color(128, 128, 128)
    colored_text = mycolor(text)
    assert colored_text == f"{CSI}38;2;128;128;128m{text}{RESET_COLOR}"


def test_create_color_bold():
    text = "Hello"

    mycolor = create_color(120, 160, 200, s="b")
    colored_text = mycolor(text)
    assert (
        colored_text
        == f"{CSI}38;2;120;160;200m{BOLD}{text}{RESET_BOLD_AND_DIM}{RESET_COLOR}"
    )


def test_create_color_underline():
    text = "Hello"

    mycolor = create_color(120, 160, 200, s="u")
    colored_text = mycolor(text)
    assert (
        colored_text
        == f"{CSI}38;2;120;160;200m{UNDERLINE}{text}{RESET_UNDERLINE}{RESET_COLOR}"
    )


def test_create_color_cross():
    text = "Hello"

    mycolor = create_color(120, 160, 200, s="c")
    colored_text = mycolor(text)
    assert (
        colored_text == f"{CSI}38;2;120;160;200m{CROSS}{text}{RESET_CROSS}{RESET_COLOR}"
    )


def test_create_color_style_only():
    # Red background
    text = "Hello"

    mycolor = create_color(s="b")
    colored_text = mycolor(text)
    assert colored_text == f"{BOLD}{text}{RESET_BOLD_AND_DIM}"


def test_create_color_background():
    # Red background
    text = "Hello"

    mycolor = create_color(bg=(120, 160, 200))
    colored_text = mycolor(text)
    assert colored_text == f"{CSI}48;2;120;160;200m{text}{RESET_BACKGROUND}"

    mycolor = create_color(bg=(128, 128, 128))
    colored_text = mycolor(text)
    assert colored_text == f"{CSI}48;2;128;128;128m{text}{RESET_BACKGROUND}"


def test_create_color_signature_error():
    with pytest.raises(TypeError):
        create_color(12, 12)

    with pytest.raises(TypeError):
        create_color(12, 12, "lol")

    with pytest.raises(TypeError):
        create_color(12)
