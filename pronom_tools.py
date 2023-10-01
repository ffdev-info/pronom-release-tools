"""Tools to help work with the PRONOM release pipeline."""

import sys

from src.pronom_tools import pronom_tools

sys.dont_write_bytecode = True


def main():
    """Primary entry point for this script."""
    pronom_tools.main()


if __name__ == "__main__":
    main()
