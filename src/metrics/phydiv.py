#!/usr/bin/env python

"""
A program that takes community sequence data to calculate phylogenetic diversity and visualize
community trees
"""

# Imports
import numpy as np
import pandas as pd

from Bio.Align.Applications import MuscleCommandline
from Bio.GenBank import Record
import toytree


# Establishing the main Phydiv class
class Phydiv:
	"""
	This class takes community sequence (.fasta or .csv) and matrix occurence data (.csv) to
	produce measures of phylogenetic diversity and tree visualizations.
	"""

	default_seq = 'default_seq.csv'
	default_mat = 'default_mat.csv'

	def __init__(self, seq = default_seq, mat = default_mat):
		self.seq = seq #this can be .fasta or .csv
		self.mat = mat #this needs to be .csv
		# Include a parameter so either both are given, or both are left blank. Otherwise, an error

	def __repr__(self):
		return f"Phylogenetic diversity will be calculated using sequences in {self.seq} and communities in {self.mat}."

#	def csv_to_fasta(self):
		"""
		A function to pull GenBank sequences from accession numbers if self.seq is a .csv
		"""
#		if self.seq[-4:] == ".csv":
            #Code to pull GenBank sequences from accession numbers and write a .fasta
#            csv = pd.read_csv(self.seq)
        
#        elif self.seq[-6:] == ".fasta":
#            pass

#        else: raise Exception("Sequence file must be .csv or .fasta")


	def align(self):
		"""
		A function to produce a file of aligned sequences from MUSCLE.
		Takes a .fasta file (pass in from previous function).
		"""

	def metacomm(self):
		"""
		A function to make a metacommunity tree from the sequences.
		Prune any OTUs not in the given communities.
		Has an option to remove OTUs.
		Should raise an error if OTUs in the community matrix do not have a corresponding sequence.
		Has the option to visualize the tree.
		"""

	def comm(self):
		"""
		A function that selects present species from the tree for each community.
		Has the option to visualize those trees.
		"""

	def mpd(self):
		"""
		A function to calculate MPD for each community and return a matrix of community and values.
		"""

	def mpdaw(self):
		"""
		A function to calculate MPDaw for each community and return a matrix of community and values.
		May be combined with the MPD function with a toggle? But may be easier to keep separate.
		"""

	def faith(self):
		"""
		A function to calculate Faith's PD for each community and return a matrix of community and values.
		"""

def main():
    """
    Main function to process arguments and call the appropriate function.
    """
    
if __name__ == "__main__":
    main()

  # will be needed to run from command line





