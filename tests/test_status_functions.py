import coloring


def test_status_functions():
    text = "Hello !"
    assert (
        coloring.success(text)
        == coloring.colorize("[+]", c="green", s="b") + " " + text
    )
    assert (
        coloring.failure(text) == coloring.colorize("[-]", c="red", s="b") + " " + text
    )
    assert (
        coloring.info(text)
        == coloring.colorize("[ ]", c="dodger_blue", s="b") + " " + text
    )


def test_status_with_their_print(capsys):
    text = "Hello"

    # test success
    coloring.print_success(text, end="")
    captured = capsys.readouterr()
    assert coloring.success(text) == captured.out

    # test failure
    coloring.print_failure(text, end="")
    captured = capsys.readouterr()
    assert coloring.failure(text) == captured.out

    # test info
    coloring.print_info(text, end="")
    captured = capsys.readouterr()
    assert coloring.info(text) == captured.out
