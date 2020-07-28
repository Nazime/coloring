# Collections of scripts used to help build this library
import os
import re
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))


# Import coloring.consts by executing the file directly (to avoid errors while importing)
const_filepath = os.path.join(current_dir, "../src/coloring/consts.py")
exec(open(const_filepath).read())

re_camelcase_to_snakecase = re.compile(r"(?<!^)(?=[A-Z])")


def camelcase_to_snakecase(text):
    return re_camelcase_to_snakecase.sub("_", text).lower()


def parse_x11_rgb_colors(filepath="/etc/X11/rgb.txt"):
    """Parse x11 rgb colors /etc/X11/rgb.txt
    Args:
        filepath(str): path of rgb.txt
    Return:
        colors(dict)
    """
    colors = {}
    colors_file = open(filepath)
    # ignore first line
    colors_file.readline()
    for line in colors_file:
        # Separate RGB colors from color name
        rgb_colors, color_name = line.split("\t\t")

        # Parse colors
        red, green, blue = rgb_colors.split()
        red = int(red)
        green = int(green)
        blue = int(blue)

        # Remove last "\n" in color name
        color_name = color_name.strip()

        # There is many redundant color with different name
        # in CamelCase or snake_case. Ex "light green" "LightGreen"
        nb_upper_char = sum(1 for c in color_name if c.isupper())
        if nb_upper_char == 0:
            # format snake_case
            color_name = color_name.replace(" ", "_")
            if color_name in colors:
                if colors[color_name] != (red, green, blue):
                    raise ValueError(
                        "Find same colors with different RGB values. Debug the script."
                    )
        else:
            # format CamelCase
            color_name = camelcase_to_snakecase(color_name)
            if color_name in colors:
                if colors[color_name] != (red, green, blue):
                    raise ValueError(
                        "Find same colors with different RGB values. Debug the script."
                    )

        # Add the color
        colors[color_name] = red, green, blue
    return colors


temmplate_color_functions_header = """# NOTE: This file is generated automatically with script.py:generate_script_functions
import sys
from .consts import *


"""
template_color_functions = """{nb_hashtag}
# {color_name} #
{nb_hashtag}
def {color_name}(text: str) -> str:
    return f"{{CSI}}38;2;{red};{green};{blue}m{{text}}{{RESET_COLOR}}"


def b{color_name}(text: str) -> str:
    return f"{{BOLD}}{{CSI}}38;2;{red};{green};{blue}m{{text}}{{RESET_COLOR}}{{RESET_BOLD_AND_DIM}}"




def print_b{color_name}(*args, sep=" ", end="\\n", file=sys.stdout, flush=False):
    text = sep.join([str(e) for e in args])
    text = b{color_name}(text)
    file.write(text)
    file.write(end)
    if flush:
        file.flush()


def print_{color_name}(*args, sep=" ", end="\\n", file=sys.stdout, flush=False):
    text = sep.join([str(e) for e in args])
    text = {color_name}(text)
    file.write(text)
    file.write(end)
    if flush:
        file.flush()


"""


def generate_color_script(filepath: str):
    # OLD Function used to generate convenience_functions
    file = open(filepath, "w")
    file.write(temmplate_color_functions_header)
    for color_name, rgb_values in COLORS.items():
        nb_hashtag = "#" * (len(color_name) + 4)
        red, green, blue = rgb_values
        func_text = template_color_functions.format(
            color_name=color_name,
            red=red,
            green=green,
            blue=blue,
            nb_hashtag=nb_hashtag,
        )
        file.write(func_text)
    file.flush()


def check_duplicate_colors():
    redundant_colors = {}
    for color_name, rgb_colors in parse_x11_rgb_colors().items():
        if rgb_colors not in redundant_colors:
            redundant_colors[rgb_colors] = [color_name]
        else:
            redundant_colors[rgb_colors].append(color_name)
    double = [e for e in redundant_colors.values() if len(e) > 1]
    print("Nomber of duplicate", len(double))


def filter_colors(colors):
    grouped_colors = {}
    for color_name, color in colors.items():
        if color not in grouped_colors:
            grouped_colors[color] = [color_name]
        else:
            grouped_colors[color].append(color_name)
    redundent_colors = [v for k, v in grouped_colors.items() if len(v) > 1]
    return grouped_colors


def filter_colors_with_digit(colors):
    # 658
    keep_colors = {}
    for color_name, color in colors.items():
        add = True
        for c in color_name:
            if c.isdigit():
                add = False
                break
        if add:
            keep_colors[color_name] = color
    return keep_colors


def generate_color_script_limited(filepath):
    file = open(filepath, "w")
    header = """# FILE GENERATED AUTOMATICALLY WITH script.py:generate_color_script_limited
from .coloring import create_print, create_color

"""
    file.write(header)
    template_function = """{color_title}
# {color} #
{color_title}
{color} = create_color("{color}", name="{color}")
b{color} = create_color("{color}", s="b", name="b{color}")
print_{color} = create_print("{color}", name="print_{color}")
print_b{color} = create_print("{color}", s="b", name="print_b{color}")


"""
    colors = filter_colors_with_digit(COLORS)
    colors = sorted(list(colors))
    # print(list(colors))
    for color in colors:
        color_title = "#" * (len(color) + 4)
        # print(repr(color))
        file.write(template_function.format(color=color, color_title=color_title))

    file.flush()
    os.system(f"black {filepath}")
    print(f"File generated at {filepath}")


if __name__ == "__main__":

    filepath_for_generate_script = os.path.join(
        current_dir, "../src/coloring/automatic_generated_convenience_functions.py"
    )
    generate_color_script_limited(filepath_for_generate_script)
