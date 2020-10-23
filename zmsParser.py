#!/usr/bin/env python3
import argparse
import base
import utils
from LDA import heuristics
from readData import read_txt


def main():
    args = argparse.ArgumentParser()
    args.add_argument("task", help=base.helpTask)
    args.add_argument("--path", "-p", nargs="?", default=base.path, help=base.helpPath)
    args.add_argument(
        "--topics", "-t", nargs="?", default=base.numberTopics, help=base.helpTopics
    )

    pargs = args.parse_args()

    if pargs.task == "run":
        print("[Running the model] it may take a while. Hang tight!")
        distributions = heuristics()
        pass
    elif pargs.task == "delete":
        # DELETE STUFF HERE
        pass
    elif pargs.task == "display":
        # DISPLAY STUFF HERE
        pass


if __name__ == "__main__":
    main()
