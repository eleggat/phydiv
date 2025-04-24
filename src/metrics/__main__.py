#!/usr/bin/env python

"""
Command line interface to Phydiv
"""

import argparse
from phydiv import Phydiv


def parse_command_line():
    "parses args for the Phydiv class"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
    	"-t",
        "--tree",
        help="Metacommunity tree. Should be Newick, NHX, or Nexus format. If given, --matrix must also be given.",
        dest='tree', type=str, default='default_tree.nwk')

    parser.add_argument(
    	"-m",
        "--matrix",
        help="Site-by-OTU matrix of communities. Must be a CSV. If given, --tree must also be given.",
        dest='matrix', type=str, default='default_matrix.csv')

    #parser.add_argument(
   # 	"--rmotu",
   # 	help="OTUs to remove from the metacommunity.",
   # 	dest='rmotu', type=str)

    parser.add_argument(
        "-p",
        "--plot"
        help="Plotting options for communities. Options: plot all communities on metacommunity phylogeny as a heatmap ('all'); plot metacommunity phylogeny with tips highlighted for one community ('highlight'); plot pruned trees for up to four communities ('prune'). *Optional*",
        dest='plot', type=str) #needs option for plotting to file

    parser.add_argument(
        "-d",
        "--diversity"
        help="Write diversity metrics (Faith's PD, MPD, and MNTD) to given csv name. *Optional*",
        dest='metric', type=str)


if __name__ == "__main__":
    args = parse_command_line()
    


