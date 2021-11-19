import pytest
from coloring.coloring import check_color, check_colors, normalize_color, parse_style
from coloring.consts import *


def test_parse_style_redundant_error():
    # Test when we call 2 times the same style
    with pytest.raises(ValueError):
        parse_style("bb")


def test_parse_style_unrecognized_style_error():
    # Test when we call 2 times the same style
    with pytest.raises(ValueError):
        parse_style("z")


def test_parse_style():
    pre, post = parse_style("b")
    assert pre == BOLD
    assert post == RESET_BOLD_AND_DIM

    pre, post = parse_style("c")
    assert pre == CROSS
    assert post == RESET_CROSS


def test_parse_style_order():
    # Oreder is important so that it is possible to test the code
    pre, post = parse_style("bu")
    assert pre == f"{UNDERLINE}{BOLD}"
    assert post == f"{RESET_BOLD_AND_DIM}{RESET_UNDERLINE}"


def test_normalize_color_unrecognized_color():
    # Test when we call 2 times the same style
    with pytest.raises(ValueError):
        normalize_color("not_existing_color")


def test_normalize_tuple_not_length_3():
    # Test when we call 2 times the same style
    with pytest.raises(ValueError):
        normalize_color((0, 0, 0, 0))

    with pytest.raises(ValueError):
        normalize_color((0, 0))

    with pytest.raises(ValueError):
        normalize_color((0,))


def test_normalize_wrong_type():
    # Test when we call 2 times the same style
    with pytest.raises(TypeError):
        normalize_color(23)

    with pytest.raises(TypeError):
        normalize_color(1.0)

    with pytest.raises(TypeError):
        normalize_color({})


def test_check_colors_bad_range():
    # red
    with pytest.raises(ValueError):
        check_colors(300, 0, 0)

    with pytest.raises(ValueError):
        check_colors(256, 0, 0)

    with pytest.raises(ValueError):
        check_colors(-1, 0, 0)

    # green
    with pytest.raises(ValueError):
        check_colors(0, 300, 0)

    with pytest.raises(ValueError):
        check_colors(0, 256, 0)

    with pytest.raises(ValueError):
        check_colors(0, -1, 0)

    # blue
    with pytest.raises(ValueError):
        check_colors(0, 0, 300)

    with pytest.raises(ValueError):
        check_colors(0, 0, 256)

    with pytest.raises(ValueError):
        check_colors(0, 0, -1)


def test_check_color():
    with pytest.raises(ValueError):
        check_color(-1)

    with pytest.raises(ValueError):
        check_color(256)

    with pytest.raises(ValueError):
        check_color(300)

    check_color(123)


def test_normalize_hex():
    assert normalize_color("#000000") == (0, 0, 0)
