from coloring import (
    blink,
    bold,
    colorize,
    cross,
    dim,
    double_underline,
    italic,
    rmbackground,
    rmblink,
    rmbold_and_dim,
    rmcolor,
    rmcross,
    rmgraphics,
    rmitalic,
    rmunderline,
    underline,
)
from coloring.consts import *


def test_rmcolor():
    text = "Hello"
    assert rmcolor(colorize(text, c="green")) == text
    assert rmcolor(colorize(text, c="red")) == text


def test_rmcolor_02():
    text = "Hello"
    # 24 bits color with 3 params
    assert rmcolor(f"{CSI}38;5;128m{text}{RESET_COLOR}") == text
    # 24 bits color with 3 params + BOLD
    assert (
        rmcolor(f"{CSI}{N_BOLD};38;5;128m{text}{RESET_COLOR}{RESET_BOLD_AND_DIM}")
        == f"{CSI}{N_BOLD}m{text}{RESET_BOLD_AND_DIM}"
    )
    # 8  colors
    for background_number in range(30, 38):
        assert rmcolor(f"{CSI}{background_number}m{text}{RESET_COLOR}") == text


def test_rmbackground():
    text = "Hello"
    assert rmbackground(colorize(text, bg="green")) == text
    assert rmbackground(colorize(text, bg="red")) == text


def test_rmbackground_02():
    text = "Hello"
    # 24 bits color with 3 params
    assert rmbackground(f"{CSI}48;5;128m{text}{RESET_BACKGROUND}") == text
    # 24 bits color with 3 params + BOLD
    assert (
        rmbackground(
            f"{CSI}{N_BOLD};48;5;128m{text}{RESET_BACKGROUND}{RESET_BOLD_AND_DIM}"
        )
        == f"{CSI}{N_BOLD}m{text}{RESET_BOLD_AND_DIM}"
    )
    # 8  colors
    for background_number in range(40, 48):
        assert (
            rmbackground(f"{CSI}{background_number}m{text}{RESET_BACKGROUND}") == text
        )


def test_rmbold_and_dim():
    text = "Hello"
    assert rmbold_and_dim(bold(text)) == text

    assert rmbold_and_dim(dim(text)) == text


def test_rmunderline():
    text = "Hello"
    assert rmunderline(underline(text)) == text

    assert rmunderline(double_underline(text)) == text


def test_rmblink():
    text = "Hello"
    assert rmblink(blink(text)) == text


def test_rmcross():
    text = "Hello"
    assert rmcross(cross(text)) == text


def test_rmcross_many_styles_in_same_sequence():
    text = "Hello"
    assert (
        rmcross(f"{CSI}{N_BOLD};{N_CROSS}m{text}{RESET_CROSS}{RESET_BOLD_AND_DIM}")
        == f"{BOLD}{text}{RESET_BOLD_AND_DIM}"
    )


def test_rmitalic():
    text = "Hello"
    assert rmitalic(italic(text)) == text


def test_rmitalic_multiple_styles():
    text = "Hello"
    assert rmitalic(cross(italic(text))) == cross(text)
    assert rmitalic(bold(italic(text))) == bold(text)
    assert rmitalic(dim(italic(text))) == dim(text)
    assert rmitalic(blink(italic(text))) == blink(text)
    assert rmitalic(underline(italic(text))) == underline(text)
    assert rmitalic(double_underline(italic(text))) == double_underline(text)

    # more than one in a raw
    assert rmitalic(bold(dim(italic(text)))) == bold(dim(text))
    assert rmitalic(blink(underline(double_underline(bold(italic(text)))))) == blink(
        underline(double_underline(bold(text)))
    )

    # other syntax
    assert rmitalic(colorize(text, s="bic")) == colorize(text, s="bc")
    assert rmitalic(colorize(text, s="bicuU")) == colorize(text, s="bcuU")


def test_rmgraphics():
    text = "Hello"
    assert rmgraphics(underline(bold(text))) == text
    assert rmgraphics(italic(colorize(text))) == text
    assert rmgraphics(colorize(text, c="red", s="uUcb", bg="yellow")) == text
    assert rmgraphics(colorize(text, c=(23, 12, 34), s="i", bg="red")) == text
