import sys

from .consts import *

# ============= #
# ATOMIC STYLES #
# ============= #


# ================== #
# INTERNAL FUNCTIONS #
# ================== #
def get_ansi_escape(
    *, c: Color = None, bg: Color = None, s: str = None
) -> Tuple[str, str]:
    """
    Return the ansi escape text before and after the text, based on the color, style and background.
    Args:
        c: color (foreground) of the text
        s: style (bold, italic, ...) of the text
        bg: color of the background of the text

    Returns:

    """
    pre_ansi_escape = ""
    post_ansi_escape = ""
    if c:
        red, green, blue = normalize_color(c)

        pre_ansi_escape += f"{CSI}38;2;{red};{green};{blue}m"
        post_ansi_escape = RESET_COLOR + post_ansi_escape

    if bg:
        red, green, blue = normalize_color(bg)

        pre_ansi_escape += f"{CSI}48;2;{red};{green};{blue}m"
        post_ansi_escape = RESET_BACKGROUND + post_ansi_escape

    if s:
        pre_style, post_style = parse_style(s)
        pre_ansi_escape += pre_style
        post_ansi_escape = post_style + post_ansi_escape

    return pre_ansi_escape, post_ansi_escape


def parse_style(s: str):
    """Parse style and return ansi escape before and after the text
    Example
        parse_style("cb") -> ("{BOLD}{CROS}", "{RESET_BOLD}{RESET_CROSS}")

    """
    if len(set(s)) != len(s):
        raise ValueError(f"style {s} contain redundant styles!")

    style_set = {}
    reset_set = {}

    for style in s:
        try:
            style_set[STYLE_MAP[style]] = None
            reset_set[STYLE_RESET_MAP[style]] = None
        except KeyError:
            raise ValueError(f"Style {style!r} in {s!r} not recognized")
    # reverse the order of resets so that each style will
    # be in a form of parentheses (easier to test)
    styles = "".join(list(reversed(list(style_set))))
    resets = "".join(reset_set)
    return styles, resets


def normalize_color(color: Color) -> tuple:
    # TODO: fix me (don't accept int)
    if isinstance(color, str):
        try:
            return COLORS[color]
        except KeyError:
            raise ValueError(f"color {color!r} not recognized")
    elif isinstance(color, tuple):
        if len(color) == 3:
            check_colors(*color)
            return color
        else:
            raise ValueError(f"color tuple must be of length 3 not {len(color)}")
    else:
        raise TypeError(f"Color must be of type str or tuple not {type(color)!r}")


def check_color(color: int):
    if not 0 <= color < 256:
        raise ValueError(f"color {color} not between 0 and 255")


def check_colors(red: int, green: int, blue: int):
    if not 0 <= red < 256:
        raise ValueError(f"red {red} not between 0 and 255")
    if not 0 <= green < 256:
        raise ValueError(f"green {green} not between 0 and 255")
    if not 0 <= blue < 256:
        raise ValueError(f"blue {blue} not between 0 and 255")


# ============== #
# MAIN FUNCTIONS #
# ============== #
def cprint(
    *text,
    c: Color = None,
    bg: Color = None,
    s: str = None,
    end: str = "\n",
    sep: str = " ",
    file=sys.stdout,
    flush: bool = False,
):
    text = sep.join([str(e) for e in text])
    pre_ansi_escape, post_ansi_escape = get_ansi_escape(c=c, bg=bg, s=s)

    # TODO: test order of end
    file.write(pre_ansi_escape)
    file.write(text)
    file.write(post_ansi_escape)
    file.write(end)
    if flush:
        file.flush()


def rgbprint(
    red: int,
    green: int,
    blue: int,
    *args,
    bg: Color = None,
    s: str = None,
    end: str = "\n",
    sep: str = " ",
    file=sys.stdout,
    flush: bool = False,
):
    cprint(
        *args,
        c=(red, green, blue),
        bg=bg,
        s=s,
        end=end,
        sep=sep,
        file=file,
        flush=flush,
    )


def colorize(text: str, c: Color = None, bg: Color = None, s: str = None) -> str:
    """
    Return a colorized string
    Args:
        text: text to colorize
        c: color
        bg: background color
        s: style to apply (bold, italic, ...)

    Returns:

    """
    pre_ansi_escape, post_ansi_escape = get_ansi_escape(c=c, bg=bg, s=s)
    return f"{pre_ansi_escape}{text}{post_ansi_escape}"


def create_color(
    color_or_red: Union[int, Color] = None,
    green: int = None,
    blue: int = None,
    *,
    bg: Color = None,
    s: str = None,
    name: str = None,
):
    """
    Create a function that colorize
    # TODO: complete doc
    Args:
        name:
        color_or_red:
        green:
        blue:
        bg:
        s:

    Returns:

    """
    if color_or_red is not None and green is None and blue is None:
        # Only the first argument is not None, so it's a string or a tuple
        color = normalize_color(color_or_red)
    elif color_or_red is not None and green is not None and blue is not None:
        # All argument are set => color is a tuple of red, green, blue
        color = normalize_color((color_or_red, green, blue))
    elif color_or_red is None and green is None and blue is None:
        # No argument is given (chose between style and background) do nothing
        color = None
    else:
        raise TypeError(
            f"Wrong signature of function create_color. For positional arguments, accept one string, one tuple, or three int"
        )

    pre_ansi_escape, post_ansi_escape = get_ansi_escape(c=color, bg=bg, s=s)

    def color_func(text):
        return f"{pre_ansi_escape}{text}{post_ansi_escape}"

    if name:
        color_func.__name__ = name
    return color_func


def create_print(
    color_or_red: Union[int, Color] = None,
    green: int = None,
    blue: int = None,
    *,
    bg: Color = None,
    s: str = None,
    name: str = None,
):
    if color_or_red is not None and green is None and blue is None:
        # Only the first argument is not None, so it's a string or a tuple
        color = normalize_color(color_or_red)
    elif color_or_red is not None and green is not None and blue is not None:
        # All argument are set => color is a tuple of red, green, blue
        color = normalize_color((color_or_red, green, blue))
    elif color_or_red is None and green is None and blue is None:
        # No argument is given (chose between style and background) do nothing
        color = None
    else:
        raise TypeError(
            f"Wrong signature of function create_color. For positional arguments, accept one string, one tuple, or three int"
        )

    pre_ansi_escape, post_ansi_escape = get_ansi_escape(c=color, bg=bg, s=s)

    def print_func(
        *text, end: str = "\n", sep: str = " ", file=sys.stdout, flush: bool = False
    ):
        text = sep.join([str(e) for e in text])

        file.write(pre_ansi_escape)
        file.write(text)
        file.write(post_ansi_escape)
        file.write(end)
        if flush:
            file.flush()

    if name:
        print_func.__name__ = name
    return print_func


def gradient(text, fc: Color, tc, f_bg=None, t_bg=None, s: str = None):
    # TODO: add background gradient
    # TODO: add many colors for the gradient
    # TODO: check errors

    fred, fgreen, fblue = normalize_color(fc)
    tred, tgreen, tblue = normalize_color(tc)

    len_minus_one = len(text) - 1
    step_red = (tred - fred) / len_minus_one
    step_green = (tgreen - fgreen) / len_minus_one
    step_blue = (tblue - fblue) / len_minus_one

    if f_bg:
        bg_fred, bg_fgreen, bg_fblue = normalize_color(f_bg)
        bg_tred, bg_tgreen, bg_tblue = normalize_color(t_bg)
        step_bg_red = (bg_tred - bg_fred) / len_minus_one
        step_bg_green = (bg_tgreen - bg_fgreen) / len_minus_one
        step_bg_blue = (bg_tblue - bg_fblue) / len_minus_one
    else:
        bg = None

    colored_text = ""
    i = 0
    for c in text:
        if f_bg:
            bg = (
                int(bg_fred + step_bg_red * i),
                int(bg_fgreen + step_bg_green * i),
                int(bg_fblue + step_bg_blue * i),
            )
        colored_text += colorize(
            c,
            c=(
                int(fred + step_red * i),
                int(fgreen + step_green * i),
                int(fblue + step_blue * i),
            ),
            s=s,
            bg=bg,
        )
        i += 1
    return colored_text


def print_gradient(text, *, fc: str, tc: str):
    print(gradient(text, fc, tc))
