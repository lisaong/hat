#!/usr/bin/env python3

"""Combines multiple HAT packages into a Statically-linked HAT package

To create a Dynamically-linked HAT package, run hat_to_dynamic.py on the resulting HAT package

Dependencies on Windows:
* the lib.exe command-line archiver, available with Microsoft Visual Studio  

Dependencies on Linux / macOS:
* the ar command-line archiver
"""

import argparse
import os
import sys

if __package__:
    from .hat_file import HATFile
    from .utilities import get_platform
else:
    from hat_file import HATFile
    from utilities import get_platform

# steps:
# 1. combine into a multi-module header, honoring the function order
# 2. run archiver

def parse_args():
    """Parses and checks the command line arguments"""
    parser = argparse.ArgumentParser(description="Creates a dynamically-linked HAT package from a statically-linked HAT package. Example:"
        "    python hat_to_dynamic.py input.hat output.hat")

    parser.add_argument("input_hat_path", type=str, help="Path to the existing HAT file, which represents a statically-linked HAT package")
    parser.add_argument("output_hat_path", type=str, help="Path to the new HAT file, which will represent a dynamically-linked HAT package")
    args = parser.parse_args()

    # check args
    if not os.path.exists(args.input_hat_path):
        sys.exit(f"ERROR: File {args.input_hat_path} not found")

    if os.path.abspath(args.input_hat_path) == os.path.abspath(args.output_hat_path):
        sys.exit("ERROR: Output file must be different from input file")

    _, extension = os.path.splitext(args.input_hat_path)
    if extension != ".hat":
        sys.exit(f"ERROR: Expected input file to have extension .hat, but received {extension} instead")

    _, extension = os.path.splitext(args.output_hat_path)
    if extension != ".hat":
        sys.exit(f"ERROR: Expected output file to have extension .hat, but received {extension} instead")

    return args


def main():
    args = parse_args()
    # create_combined_package(args.input_hat_paths, args.output_hat_path)


if __name__ == "__main__":
    main()
