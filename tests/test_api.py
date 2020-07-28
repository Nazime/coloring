import coloring

text = "Hello Word!"


def test_simple_print():
    coloring.print_green(text)
    coloring.print_red(text)


def test_convenience_functions():
    coloring.print_success("Yes")
    coloring.print_failure("Nop")
    coloring.print_info("yop")
