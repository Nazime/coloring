from .automatic_generated_convenience_functions import bdodger_blue, bgreen, bred
from .coloring import create_color, create_print

bold = create_color(s="b")
dim = create_color(s="d")
underline = create_color(s="u")
double_underline = create_color(s="U")
italic = create_color(s="i")
cross = create_color(s="c")
blink = create_color(s="k")


print_bold = create_print(s="b")
print_dim = create_print(s="d")
print_underline = create_print(s="u")
print_double_underline = create_print(s="U")
print_italic = create_print(s="i")
print_cross = create_print(s="c")
print_blink = create_print(s="k")


def print_success(*args, **kwargs):
    print(bgreen("[+]"), *args, **kwargs)


def print_failure(*args, **kwargs):
    print(bred("[-]"), *args, **kwargs)


def print_info(*args, **kwargs):
    print(bdodger_blue("[ ]"), *args, **kwargs)
