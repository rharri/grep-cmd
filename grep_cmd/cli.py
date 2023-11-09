import argparse
import re
from collections import namedtuple

Options = namedtuple("Options", "pattern, file")


def main() -> int:
    """Entry point for grep_cmd."""
    parser = argparse.ArgumentParser("grep",
                                     description="Search input file, selecting lines that match a pattern.",
                                     usage="grep [pattern] [file ...]")

    parser.add_argument("pattern")
    parser.add_argument("file")

    options = Options(**vars(parser.parse_args()))

    user_pattern = re.compile(options.pattern)

    with open(options.file, "r") as f:
        for line in f.readlines():
            if user_pattern.search(line):
                print(line, end="")

    return 0
