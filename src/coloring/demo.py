import shutil

from .coloring import colorize, cprint
from .consts import *


def demo_colors(*, word_per_line: int = None, colors=None, bg=None, s: str = None):
    if colors is None:
        colors = COLORS
    i_word = 1
    i_word_per_line = 1
    i_line = 0
    msg = f"{i_line} "
    print(f"{len(colors)} colors available: ")

    max_len_word = len(max(colors, key=len)) + 1

    # get the longest word
    if word_per_line is None:
        terminal_size = shutil.get_terminal_size().columns
        word_per_line = terminal_size // max_len_word
    for color_name in sorted(colors):
        cprint(color_name.ljust(max_len_word), c=color_name, bg=bg, s=s, end="")
        if i_word_per_line == word_per_line:
            print()
            i_word_per_line = 0
            i_line += 1

        i_word_per_line += 1
        i_word += 1
    print()


def demo_colors_old(word_per_line=10):
    i = 0
    i_word_per_line = 0
    word_per_line = 10
    i_line = 0
    msg = f"{i_line} "
    for red in range(0, 256, 10):
        for green in range(0, 256, 10):
            for blue in range(0, 256, 10):
                word = rgb_color(red, green, blue, f"Hello {i}")
                msg += BOLD + word + RESET_COLOR + " "
                if i_word_per_line == word_per_line:
                    print(msg)
                    msg = f"{i_line} "
                    i_word_per_line = 0
                    i_line += 1

                i_word_per_line += 1
                i += 1


def printe_gradiant(text):
    colored_text = ""
    i = 0
    for c in text:
        colored_text += colorize(c, c=(120 + i, 128, 200))
        i += 2
    print(colored_text)
