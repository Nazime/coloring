import coloring

text = "Hello Word!"


def test_simple_print():
    coloring.print_green(text)
    coloring.print_red(text)


def test_status_functions():
    coloring.success("Yes")
    coloring.failure("Nop")
    coloring.info("yop")


def test_print_status_functions():
    coloring.print_success("Yes")
    coloring.print_failure("Nop")
    coloring.print_info("yop")
