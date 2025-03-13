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
        help="Number of tips in the metacommunity phylogeny (number of species). Default 100.",
        dest='ntips', type=int, default=100)

    parser.add_argument(
        "--sr",
        help="Species richness of the simulated community. Has no default value and must be specified. sr must be < ntips.",
        dest='sr', type=int, required=True)

    parser.add_argument(
        "--pa",
        help="Phylogenetic assumption of the community simulation. -1: related species are least likely to co-occur; 0: no phylogenetic structure; 1: related species are most likely to co-occur. Default 0.",
        dest='pa', type=float, default = 0)

    parser.add_argument(
        "--nsites",
        help="Number of sites (rows) to simulate for the site by species matrix. Default 10.",
        dest='nsites', type=int, default = 10)

    parser.add_argument(
        "--df",
        help="Community simulation output is a numpy array when False. Output is a numpy array when True. Default False.", 
        dest='df', type=bool, default=True)

    parser.add_argument(
        "--csv",
        help="When given, output is written to a csv file with specified str name. Do not include .csv extension in file name.", 
        dest='csv', type=str, default=None)

    parser.add_argument(
        "-v", "--verbose", 
        help="Increase output verbosity",
        dest = "verbose", action="store_true")

    # parse args
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line()
    print(Simpd(ntips = args.ntips))
    print(Simpd(ntips = args.ntips).simmat(sr = args.sr, pa = args.pa, nsites = args.nsites, df = args.df, csv = args.csv))
