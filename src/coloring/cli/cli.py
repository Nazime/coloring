import argparse
import sys
from typing import Tuple

import coloring

help = """usage: coloring [-h] <subcommand>


Colorize text using ANSI escape and remove graphics.


colors commands:
    colorize            Generic command to colorize text
    <color>             Convenience command to colorize with specific color
                        use list to see available colors
    b<color>            Convenience command to colorize with specific color and bold style
                        use list to see available colors
    list                List default colors (used with convenience commands)

styles commands:
    bold                Apply bold style
    dim                 Apply dim style
    cross               Apply cross style
    blink               Apply blink style
    underline           Apply underline style
    double_underline    Apply double_underline style
    italic              Apply italic style

remove graphics sub commands:
    rmgraphics          Remove all graphics (colors, styles, background)
    rmcolor             Remove colors
    rmbackground        Remove background
    rmstyle             Remove all styles
    rmblink             Remove blink style
    rmbold_and_dim      Remove bold and dim styles
    rmcross             Remove cross style
    rmitalic            Remove italic style
    rmunderline         Remove underline and double underline styles

optional arguments:
  -h, --help            show this help message and exit
"""


def normalize_color(color: str) -> coloring.consts.Color:
    if "," in color:
        r, g, b = color.split(",")
        r = int(r)
        g = int(g)
        b = int(b)
        return r, g, b
    return color


class SubcmdHelper:
    # parser_x(self, parser)
    # run_x(self, args)
    # help_x = "lol"
    prog = None

    def __init__(self):
        self.main_parser = argparse.ArgumentParser(self.prog)
        self.subparsers = self.main_parser.add_subparsers(dest="subcommand")
        for subparser_func_name in [
            e
            for e in dir(self)
            if e.startswith("parser_") and callable(getattr(self, e))
        ]:
            subparser_func = getattr(self, subparser_func_name)
            subparser_name = subparser_func_name[len("parser_") :]
            help = getattr(self, "help_" + subparser_name, None)
            subparser = self.subparsers.add_parser(
                subparser_name, help=help, description=help
            )
            subparser_func(subparser)

    def main(self, args=None):
        parsed_args = self.main_parser.parse_args(args)
        subcommand_name = parsed_args.subcommand
        if subcommand_name is None:
            self.main_parser.print_help()
            return

        try:
            subcommand = getattr(self, f"run_{subcommand_name}")
            if not callable(subcommand):
                raise TypeError(f"{subcommand_name} attribute must be callable")

        except AttributeError:
            if hasattr(self, f"parser_{subcommand_name}"):
                print(f"Command {subcommand_name} not implemented")
                self.main_parser.print_usage()
                return
            else:
                # FIXME: dead code, argparse handle this case
                print(f"Command {subcommand_name} don't exist")
                self.main_parser.print_usage()
                return
        subcommand(parsed_args)
        return


class ColoringSubcmdHelper(SubcmdHelper):
    prog = "coloring"

    def parser_list(self, parser):
        parser.add_argument("-s", "--style", help="Style to colors")
        parser.add_argument("-b", "--background", help="background to colors")

    def run_list(self, args):
        # TODO: implement me
        coloring.demo_colors(
            colors=coloring.DEFAULT_COLORS, s=args.style, bg=args.background
        )

    def parser_colorize(self, parser):
        # stdin empty
        if sys.stdin.isatty():
            # If stdin is empty we wait the next argument to be a string
            # otherwise we do nothing since the text is in stdin
            parser.add_argument("text", help=f"Text to colorize")
        parser.add_argument("-c", "--color", help="color to apply")
        parser.add_argument("-s", "--style", help="style to apply")
        parser.add_argument("-b", "--background", help="background color to apply")
        # TODO: refactor -n argument and add it to other functions
        # TODO: test the CLI
        # TODO: speed the project? (build it over again? or an other project!)
        parser.add_argument("-n", action="store_true", help="don't print new line")

    def run_colorize(self, args):
        if args.color:
            args.color = normalize_color(args.color)
        if args.background:
            args.background = normalize_color(args.background)
        if args.n:
            end = ""
        else:
            end = "\n"
        if sys.stdin.isatty():
            print(
                coloring.colorize(
                    args.text, c=args.color, bg=args.background, s=args.style
                ),
                end=end,
            )
        else:
            for line in sys.stdin:
                print(
                    coloring.colorize(
                        line, c=args.color, bg=args.background, s=args.style
                    ),
                    end="",
                )


def add_colors_styles_rmgraphics_subcommands(cls):
    commands = {}
    for style in coloring.consts.STYLES:
        commands[style] = f"Apply {style} style"

    # add rmgraphics
    rmgrphics = {
        "rmgraphics": "Remove all graphics",
        "rmcolor": "Remove colors",
        "rmbackground": "Remove background",
        "rmstyle": "Remove all styles",
        "rmblink": "Remove blink style",
        "rmbold_and_dim": "Remove bold and dim styles",
        "rmcross": "Remove cross style",
        "rmitalic": "Remove italic style",
        "rmunderline": "Remove underline and double underline styles",
    }
    commands.update(rmgrphics)

    # add colors
    for color in coloring.DEFAULT_COLORS:
        commands[color] = f"Colorize text with {color} color"
        commands["b" + color] = f"Colorize text with {color} color and bold style"

    import pprint

    # pprint.pprint(commands)

    # we must use function factory otherwise variable inside
    # functions will change -
    # https://stackoverflow.com/questions/3431676/creating-functions-in-a-loop
    def make_parser_command(command_help):
        def parser_command(self, parser):
            if sys.stdin.isatty():
                # If stdin is empty we wait the next argument to be a string
                # otherwise we do nothing since the text is in stdin
                parser.add_argument("text", help=command_help)

        return parser_command

    def make_run_command(func):
        def run_command(self, args):
            if sys.stdin.isatty():
                print(func(args.text))
            else:
                for line in sys.stdin:
                    print(func(line), end="")

        return run_command

    for command_name, command_help in commands.items():
        func = getattr(coloring, command_name)
        setattr(cls, f"parser_{command_name}", make_parser_command(command_help))
        setattr(cls, f"run_{command_name}", make_run_command(func))


def main():
    add_colors_styles_rmgraphics_subcommands(ColoringSubcmdHelper)
    subcmd_helper = ColoringSubcmdHelper()
    main_parser = subcmd_helper.main_parser
    main_parser.print_help = lambda file=None: print(help, file=file)
    main_parser.print_usage = subcmd_helper.main_parser.print_help

    # monkey patch
    _error = main_parser.error

    def error(message):
        if "argument subcommand: invalid choice" in message:
            print(help)
            print(f"{main_parser.prog}: error: invalid subcommand '{sys.argv[1]}'\n")
            sys.exit(2)
        else:
            _error(message)

    subcmd_helper.main_parser.error = error
    subcmd_helper.main()


if __name__ == "__main__":
    main()
