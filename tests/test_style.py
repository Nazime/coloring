from coloring import blink, bold, cross, dim, double_underline, underline
from coloring.consts import *


def test_underline():
    text = "Hello"
    styled_text = underline(text)
    assert styled_text == f"{UNDERLINE}{text}{RESET_UNDERLINE}"


def test_bold():
    text = "Hello"
    styled_text = bold(text)
    assert styled_text == f"{BOLD}{text}{RESET_BOLD_AND_DIM}"


def test_dim():
    text = "Hello"
    styled_text = dim(text)
    assert styled_text == f"{DIM}{text}{RESET_BOLD_AND_DIM}"


def test_double_underline():
    text = "Hello"
    styled_text = double_underline(text)
    assert styled_text == f"{DOUBLE_UNDERLINE}{text}{RESET_UNDERLINE}"


def test_cross():
    text = "Hello"
    styled_text = cross(text)
    assert styled_text == f"{CROSS}{text}{RESET_CROSS}"


def test_blink():
    text = "Hello"
    styled_text = blink(text)
    assert styled_text == f"{BLINK}{text}{RESET_BLINK}"


def test_many():
    text = "Hello"
    styled_text = underline(cross(text))
    assert styled_text == f"{UNDERLINE}{CROSS}{text}{RESET_CROSS}{RESET_UNDERLINE}"
