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
    	"-s",
        "--seq",
        help="Sequences for metacommunity OTUs. Can be a CSV of GenBank accession numbers or a FASTA of sequences.",
        dest='seq', type=str, default='default_seq.csv')

    parser.add_argument(
    	"-m",
        "--matrix",
        help="Site-by-OTU matrix of communities. Must be a CSV.",
        dest='mat', type=str, default='default_mat.csv')

    parser.add_argument(
    	"--rmotu",
    	help="OTUs to remove from the metacommunity.",
    	dest='rmotu', type=str)

    parser.add_argument(
        "--metric",
        help="Phylogenetic metrics to calculate for each community.",
        dest='metric', type=str)