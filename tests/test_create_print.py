import io

import pytest
from coloring import create_print
from coloring.consts import *


def test_create_print_simple():
    text = "Hello"

    myprint = create_print(120, 160, 200)
    f = io.StringIO()
    myprint(text, file=f)
    captured_stdout = f.getvalue()

    assert captured_stdout == f"{CSI}38;2;120;160;200m{text}{RESET_COLOR}\n"


def test_create_print_print_signature():
    # Test if the create_print return the same signature as print
    text = "Hello"

    myprint = create_print()
    f = io.StringIO()
    myprint(text, text, text, file=f)
    captured_stdout = f.getvalue()
    assert captured_stdout == f"{text} {text} {text}\n"

    # test sep
    f = io.StringIO()
    myprint(text, text, text, sep=",", file=f)
    captured_stdout = f.getvalue()
    assert captured_stdout == f"{text},{text},{text}\n"

    # test end
    f = io.StringIO()
    myprint(text, text, text, end="", file=f)
    captured_stdout = f.getvalue()
    assert captured_stdout == f"{text} {text} {text}"

    # test 3 differents positional args
    f = io.StringIO()
    myprint(text, 123, text, file=f)
    captured_stdout = f.getvalue()
    assert captured_stdout == f"{text} 123 {text}\n"

    # flush
    f = io.StringIO()
    myprint(text, 123, text, file=f, flush=True)
    captured_stdout = f.getvalue()
    assert captured_stdout == f"{text} 123 {text}\n"


def test_create_print_complex_style_with_many_args():
    text = "Hello"

    myprint = create_print("red", bg="yellow", s="b")
    f = io.StringIO()
    myprint(text, 123, text, file=f)
    captured_stdout = f.getvalue()
    expected_result = f"{CSI}38;2;255;0;0m{CSI}48;2;255;255;0m{BOLD}{text} 123 {text}{RESET_BOLD_AND_DIM}{RESET_BACKGROUND}{RESET_COLOR}\n"
    assert captured_stdout == expected_result


def test_create_print_signature_error():
    with pytest.raises(TypeError):
        create_print(12, 12)

    with pytest.raises(TypeError):
        create_print(12, 12, "lol")

    with pytest.raises(TypeError):
        create_print(12)
