from coloring import colorize, gradient


def test_gradient_2_char():
    text = "AB"
    colored_text = gradient(text, "red", "green")
    assert colored_text == colorize("A", c="red") + colorize("B", c="green")


def test_gradient_3_char():
    text = "ABC"
    colored_text = gradient(text, "red", "green")
    expected = (
        colorize("A", c="red")
        + colorize("B", c=(127, 127, 0))
        + colorize("C", c="green")
    )
    print()
    print("result   ", repr(colored_text))
    print("expected ", repr(expected))
    assert colored_text == expected
