from .automatic_generated_convenience_functions import bdodger_blue, bgreen, bred
from .coloring import create_color, create_print, colorize
from . import consts

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
    print(
        colorize(consts.TXT_SUCCESS, c=consts.COLOR_SUCCESS, s=consts.STYLE_SUCCESS),
        *args,
        **kwargs
    )


def print_failure(*args, **kwargs):
    print(
        colorize(consts.TXT_FAILURE, c=consts.COLOR_FAILURE, s=consts.STYLE_FAILURE),
        *args,
        **kwargs
    )


def print_info(*args, **kwargs):
    print(
        colorize(consts.TXT_INFO, c=consts.COLOR_INFO, s=consts.STYLE_INFO),
        *args,
        **kwargs
    )


def success(text):
    return (
        colorize(consts.TXT_SUCCESS, c=consts.COLOR_SUCCESS, s=consts.STYLE_SUCCESS)
        + " "
        + text
    )


def failure(text):
    return (
        colorize(consts.TXT_FAILURE, c=consts.COLOR_FAILURE, s=consts.STYLE_FAILURE)
        + " "
        + text
    )


def info(text):
    return (
        colorize(consts.TXT_INFO, c=consts.COLOR_INFO, s=consts.STYLE_INFO) + " " + text
    )
