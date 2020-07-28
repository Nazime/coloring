import coloring

# NOTE: Those test are visual and should be validated by a human


def test_visual():
    print(f"This is {coloring.green('green')} and this is {coloring.red('red')}")
    coloring.print_green("All this text is green")
    coloring.print_blue("And all this text is blue")
    coloring.print_yellow("And this text is yello AND BOLD")
    print(
        "Styles",
        coloring.bold("bold"),
        "nothing",
        coloring.underline("underline"),
        "nothing",
        coloring.double_underline("double_underline"),
        "nothing",
        coloring.cross("cross"),
        "nothing",
        coloring.blink("blink"),
        "nothing",
        coloring.italic("italic"),
        "nothing",
        coloring.dim("dim"),
        "nothing",
    )
