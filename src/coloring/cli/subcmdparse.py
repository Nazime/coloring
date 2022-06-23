import argparse
import sys

import coloring


"""
Group structure:
    name(str)
    title(str)
    description(str)
    commands(dict)
        description(str)
"""


class SubcommandParser:
    def __init__(
        self,
        prog=None,
        *,
        parent=None,
        parser=None,
        autocomplete: bool = None,
        # Help
        colors=None,
        prolog=None,
        description=None,
        epilog=None,
    ):
        """

        Args:
            prog: name of the program
            parent: parent parser
            parser: argparse.ArgParser to use
            description: description of the program
            autocomplete: E,able autocomplete
            colors:

        Advantages over argparse:
            - use add_subcommand instead of using add_parsers then add_subparser
            - run command that will run directly the program
            - better help with groups/colors
            - ease of use autocomplete
        """

        if prog is None:
            prog = sys.argv[0]

        if colors is None:
            colors = False

        if autocomplete is None:
            autocomplete = False

        self.parent = parent
        self.name = prog or sys.argv[0]
        self.subcommands = {}
        self.function = None
        self._argparse_subparsers = None

        # Help
        self.colors = colors
        self.groups = {}
        self.add_group("_ungrouped", title="Other commands")
        self.description = description
        self.prolog = prolog
        self.epilog = epilog
        self.hide = False
        self.autocomplete = autocomplete
        self._group_namespace = (
            set()
        )  # track groupnamespace for subcommands and help_subcommands

        if self.parent is None:
            self.fullname = self.name
        else:
            self.fullname = f"{self.parent.fullname}.{self.name}"

        if parser is None:
            parser = argparse.ArgumentParser(
                prog=prog, description=description, epilog=epilog
            )

        self._argparse_parser = parser
        self._subcommand_depth = 1

        self._print_help = self._argparse_parser.print_help

    def add_argument(self, *args, **kwargs):
        self._argparse_parser.add_argument(*args, **kwargs)

    def add_group(self, name, *, title: str = None, description: str = None):
        if name in self.groups:
            raise KeyError(f"Group {name} already exists")

        if title is None:
            title = name

        if description is None:
            description = ""

        self.groups[name] = {"title": title, "description": description, "commands": {}}

    def add_subcommand(self, command_name, description=None, group=None, hide=False):
        if command_name in self.subcommands:
            raise KeyError(f"command {command_name!r} already exists")

        # TODO: check that help_command is not existing in the same grp
        #  refactor this! we should check all namespace not only the one for grp
        # TODO: test me
        if group and hide:
            raise ValueError(f"Canno't have both group and hide is True")
        if not hide:
            if command_name in self._group_namespace:
                raise KeyError(
                    f"command {command_name!r} already exists as help_subcommand"
                )

            if group is None:
                group = "_ungrouped"

            self.groups[group]["commands"][command_name] = {"description": description}
            self._group_namespace.add(command_name)

        if self._argparse_subparsers is None:
            self._argparse_subparsers = self._argparse_parser.add_subparsers(
                dest=self._get_subcommand_dest_name()
            )

        subcommand_parser = self._argparse_subparsers.add_parser(command_name)

        subcommand_command = SubcommandParser(
            command_name, parser=subcommand_parser, parent=self, description=description
        )
        subcommand_command._subcommand_depth += self._subcommand_depth
        subcommand_command.hide = hide
        self.subcommands[command_name] = subcommand_command
        return subcommand_command

    def add_help_subcommand(self, command_name, description=None, group=None):
        """Only add this command in the help

        Explanation:
            this could be usefull if you have a lot of commands that are hidden
            and you want to add one help description to group all these commands
        """
        if group is None:
            group = "_ungrouped"

        if command_name in self.subcommands:
            raise KeyError(f"command {command_name!r} already exists")

        if command_name in self._group_namespace:
            raise KeyError(
                f"command {command_name!r} already exists in help_subcommands"
            )

        self.groups[group]["commands"][command_name] = {"description": description}
        self._group_namespace.add(command_name)

    def __getitem__(self, item: str):
        return self.subcommands[item]

    def __str__(self):
        return f"SubcommandParser(<{self.fullname}>)"

    def __repr__(self):
        return self.__str__()

    def print_help(self):
        self._init_help()
        self._print_help()

    def _get_subcommand_dest_name(self, depth: int = None):
        if depth is None:
            depth = self._subcommand_depth
        if depth == 1:
            return "subcommand"
        else:
            return f"subcommand_{depth}"

    def _get_subcommand_name(self, parsed_args, depth: int = None):
        argparse_cmd_name = self._get_subcommand_dest_name(depth)
        return getattr(parsed_args, argparse_cmd_name)

    def parse_args(self, args=None, namespace=None):
        self.check_errors()
        self._init_help()

        if self.autocomplete:
            import argcomplete

            argcomplete.autocomplete(self._argparse_parser)

        return self._argparse_parser.parse_args(args, namespace=namespace)

    def run(self, args=None):
        """Run the main program"""

        # Parse arguments
        parsed_args = self.parse_args(args)
        # TODO: hook main: self._run_main(parsed_args)  # hook to _run_main

        # Check if there is any subcommand
        if not self.subcommands:
            self.print_help()
            sys.exit(1)

        # get called subcommand
        depth = 1
        subcommand = self
        while True:
            try:

                cmd_name = self._get_subcommand_name(parsed_args, depth=depth)

                if cmd_name is None:
                    self.print_help()
                    sys.exit(1)
                subcommand = subcommand[cmd_name]
                depth += 1
            except AttributeError:
                break

        # If function is None, automatically it (doesn't have subparsers
        #  because we already checked errors on parse_args
        if subcommand.function is None:
            self.print_help()
            sys.exit(0)

        subcommand.function(parsed_args)

    def _init_help(self):
        """If groups exist change the current help"""
        """
        - prolog
        - usage
        - prog description
        - list subcommands
        - epilog
        """
        SPACES = "    "
        LINE_SEP = "\n\n"

        # FIXME: test/me
        # Handle groups
        # =============
        # Groups are already handled in add_subcommand
        if len(self.groups) == 1:
            # If len groups == 1, title = "Commands" else title = "Other commands"
            self.groups["_ungrouped"]["title"] = "Commands"

        # make ungrouped in last position
        _ungrouped = self.groups.pop("_ungrouped")
        self.groups["_ungrouped"] = _ungrouped
        # get the longest command name for pretty print with tabulations
        # flatten all commands names in self.groups()
        commands_names = [
            cmd for group in self.groups.values() for cmd in group["commands"]
        ]

        if len(commands_names):
            max_command_length = len(max(commands_names, key=len))
        else:
            max_command_length = 0

        # header prog name and description
        prog = self.name
        help = ""

        # add prolog
        if self.prolog:
            help += self.prolog + LINE_SEP

        # add usage
        help += f"Usage: {prog} [-h] <subcommand>{LINE_SEP}"

        # add description
        if self.description:
            help += f"{self.description}{LINE_SEP}"

        for group_name, group in self.groups.items():
            if not group["commands"]:
                continue
            group_title = group["title"] + ":"
            if self.colors:
                group_title = coloring.colorize(group_title, c="slate_blue3", s="b")

            group_description = group.get("description", "")

            help += group_title
            if group_description:
                help += " " + group_description
            help += LINE_SEP
            for cmd_name, command_info in group["commands"].items():
                description_command = command_info.get("description", "") or ""
                cmd_txt = cmd_name.ljust(max_command_length)
                if self.colors:
                    cmd_txt = coloring.colorize(cmd_txt, c="medium_purple")
                help += f"{SPACES}{cmd_txt}{SPACES}{description_command}\n"
            help += "\n"

        help += self.epilog or ""
        # change the help function
        self._argparse_parser.print_help = lambda file=None: print(help, file=file)
        # self.main_parser.print_usage = self.main_parser.print_help
        # print(help)
        self._print_help = self._argparse_parser.print_help

    def _print_and_exist(self, msg, status=1):
        print(msg)
        sys.exit(status)

    def iter_allcommands(self):
        """Iter all commands, self included"""
        yield self
        for parser in self.subcommands.values():
            yield from parser.iter_allcommands()

    def check_errors(self):
        """Check if subcommands are correctly built
        This method is called before parse_args/run
        """
        for command in self.iter_allcommands():
            # If function exists it must be callable
            if command.function is not None and not callable(command.function):
                raise TypeError(f"{command.fullname}.function must be callable")

            # Todo: check that function has only one argument

            # If the command don't have any subcommand, it must have a function
            if not command.subcommands and command.function is None:
                raise ValueError(
                    f"Subcommand {command} don't have linked function or should have subpcommands"
                )
