from coloring import colorize
from coloring.consts import *
from coloring.remove_graphics import re_sgr, remove_attributes_from_sgr


def test_parse_sgr_string_simple():
    text = f"{CSI}1;2;3m"
    remove = ["2"]
    expected = f"{CSI}1;3m"
    assert expected == remove_attributes_from_sgr(text, remove)

    text = f"{CSI}1;2m"
    remove = ["3"]
    expected = f"{CSI}1;2m"
    assert expected == remove_attributes_from_sgr(text, remove)


def test_parse_sgr_remove_the_only_one():
    text = f"{CSI}1m"
    remove = ["1"]
    expected = f""
    assert expected == remove_attributes_from_sgr(text, remove)


def test_parse_sgr_remove_all():
    text = f"{CSI}1;2;3m"
    remove = ["1", "2", "3"]
    expected = f""
    assert expected == remove_attributes_from_sgr(text, remove)


def test_parse_sgr_remove_all_02():
    text = f"{CSI}1;38;5;0;2;3m"
    remove = ["1", "2", "3", "38"]
    expected = f""
    assert expected == remove_attributes_from_sgr(text, remove)


def test_parse_sgr_multiple_param_sequence_01():
    # RESETALL;BOLD;redcolor
    text = f"{CSI}1;2;38;2;255;0;0m"
    remove = ["38"]
    expected = f"{CSI}1;2m"
    assert expected == remove_attributes_from_sgr(text, remove)


def test_parse_sgr_multiple_param_sequence_02():
    # RESETALL;BOLD;redcolor
    text = f"{CSI}1;2;38;2;255;0;0;3;4m"
    remove = ["38"]
    expected = f"{CSI}1;2;3;4m"
    assert expected == remove_attributes_from_sgr(text, remove)


def test_parse_sgr_multiple_param_sequence_03():
    # RESETALL;BOLD;redcolor
    text = f"{CSI}1;2;38;5;255;3;4m"
    remove = ["38"]
    expected = f"{CSI}1;2;3;4m"
    assert expected == remove_attributes_from_sgr(text, remove)


def test_remove_attributes_from_sgr_04():
    text = f"{CSI}1;2;38;5;255;3;4m"
    remove = ["1", "2"]
    expected = f"{CSI}38;5;255;3;4m"
    assert expected == remove_attributes_from_sgr(text, remove)


def test_re_sgr():
    assert re_sgr.findall("Nothing here") == []
    assert re_sgr.findall(colorize("Hello", c="red")) == [
        f"{CSI}38;2;255;0;0m",
        RESET_COLOR,
    ]
    # TODO: test if '' is the same as '0' !
