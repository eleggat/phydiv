#!/usr/bin/env python

"""
Command line interface to Simpd
"""

import argparse
from simpd import Simpd


def parse_command_line():
    "parses args for the Simpd class"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--ntips",
        help="Number of tips in the metacommunity phylogeny (number of species)",
        dest='ntips', type=int, default=100)

    parser.add_argument(
        "--sr",
        help="Species richness of the simulated community. Has no default value. sr must be < ntips.",
        dest='sr', type=int, required=True)

    parser.add_argument(
        "--pa",
        help="Phylogenetic assumption of the community simulation. -1: related species are least likely to co-occur; 0: no phylogenetic structure; 1: related species are most likely to co-occur.",
        dest='pa', type=float, default = 0)

    parser.add_argument(
        "--df",
        help="Community simulation output is a pandas dataframe. Default True. Else, output is a numpy array.", 
        dest='df', type=bool, default=True)
    parser.add_argument(
        "-v", "--verbose", 
        help="Increase output verbosity",
        dest = "verbose", action="store_true")

    # parse args
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line()
    print(Simpd(ntips = args.ntips))
    print(Simpd(ntips = args.ntips).simmat(sr = args.sr, pa = args.pa, df = args.df))
