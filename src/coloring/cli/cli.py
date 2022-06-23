import sys

import coloring

from .subcmdparse import SubcommandParser


def normalize_color(color: str) -> coloring.consts.Color:
    if "," in color:
        r, g, b = color.split(",")
        r = int(r)
        g = int(g)
        b = int(b)
        return r, g, b
    return color


def add_colors_styles_rmgraphics_subcommands(coloring_cmd):
    commands = {}
    for style in coloring.consts.STYLES:
        func = getattr(coloring, style)
        example = func("\tExample...")
        commands[style] = {
            "description": f"Apply {style} style. {example}",
            "group": "styles",
        }

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
    for cmd_name, cmd_help in rmgrphics.items():
        commands[cmd_name] = {"description": cmd_help, "group": "rmgraphics"}

    # add colors
    for color in coloring.DEFAULT_COLORS:
        commands[color] = {"hide": True}
        commands["b" + color] = {"hide": True}

    def make_run_command(func):
        def run_command(args):
            if sys.stdin.isatty():
                print(func(args.text))
            else:
                for line in sys.stdin:
                    print(func(line), end="")

        return run_command

    for command_name, command_info in commands.items():
        func = getattr(coloring, command_name)
        subcmd = coloring_cmd.add_subcommand(
            command_name,
            group=command_info.get("group"),
            description=command_info.get("description"),
            hide=command_info.get("hide"),
        )
        if sys.stdin.isatty():
            # If stdin is empty we wait the next argument to be a string
            # otherwise we do nothing since the text is in stdin
            subcmd.add_argument("text")

        subcmd.function = make_run_command(func)


def run_colorize(args):
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
                coloring.colorize(line, c=args.color, bg=args.background, s=args.style),
                end="",
            )


def main():
    coloring_cmd = SubcommandParser(
        "coloring",
        description="Colorize text using ANSI escape and remove graphics.",
        colors=True,
    )
    coloring_cmd.add_group("basics", title="Basic commands", description="")
    coloring_cmd.add_group(
        "styles", title="Styles commands", description="Apply specific style to text"
    )
    coloring_cmd.add_group(
        "rmgraphics",
        title="Remove graphics commands",
        description="Remove specific style/color from text",
    )

    colorize_cmd = coloring_cmd.add_subcommand(
        "colorize", group="basics", description="Generic command to colorize text"
    )
    # stdin empty
    if sys.stdin.isatty():
        # If stdin is empty we wait the next argument to be a string
        # otherwise we do nothing since the text is in stdin
        colorize_cmd.add_argument("text", help=f"Text to colorize")
    colorize_cmd.add_argument("-c", "--color", help="color to apply")
    colorize_cmd.add_argument("-s", "--style", help="style to apply")
    colorize_cmd.add_argument("-b", "--background", help="background color to apply")
    # TODO: refactor -n argument and add it to other functions
    # TODO: test the CLI
    # TODO: speed the project? (build it over again? or an other project!)
    colorize_cmd.add_argument("-n", action="store_true", help="don't print new line")
    colorize_cmd.function = run_colorize

    coloring_cmd.add_help_subcommand(
        "<color>",
        description="Convenience command to colorize with specific color. Use list to see available colors",
        group="basics",
    )
    coloring_cmd.add_help_subcommand(
        "b<color>",
        description="Convenience command to colorize with specific color and bold style. Use list to see available colors",
        group="basics",
    )

    list_cmd = coloring_cmd.add_subcommand(
        "list",
        group="basics",
        description="List default colors (used with convenience commands)",
    )
    list_cmd.add_argument("-s", "--style", help="Style to colors")
    list_cmd.add_argument("-b", "--background", help="background to colors")
    list_cmd.function = lambda args: coloring.demo_colors(
        colors=coloring.DEFAULT_COLORS, s=args.style, bg=args.background
    )
    add_colors_styles_rmgraphics_subcommands(coloring_cmd)

    # monkey patch
    _error = coloring_cmd._argparse_parser.error

    def error(message):
        if "argument subcommand: invalid choice" in message:
            print(help)
            print(f"{coloring_cmd.prog}: error: invalid subcommand '{sys.argv[1]}'\n")
            sys.exit(2)
        else:
            _error(message)

    coloring_cmd._argparse_parser.error = error

    coloring_cmd.run()


if __name__ == "__main__":
    main()
