#!/usr/bin/env python

"""
A program that takes community sequence data to calculate phylogenetic diversity and visualize
community trees
"""

# Imports
import numpy as np
import pandas as pd

from Bio.Align.Applications import MuscleCommandline
import toytree


# Establishing the main Phydiv class
class Phydiv:
	"""
	This class takes community sequence (.fasta or .csv) and matrix occurence data (.csv) to
	produce measures of phylogenetic diversity and tree visualizations.
	"""

	default_seq = pd.DataFrame(data={'OTU id': ['c.glandium', 'd.plexippus', 't.sinensis'],
		'Accession number': ['KC784066.1', 'GU672935.1', 'MZ099432.1']}) #will need to make this a .csv

	default_mat = pd.DataFrame(data={'Community': ['site1', 'site2', 'site3'],
		'c.glandium': [10, 6, 2],
		'd.plexippus': [5, 0, 8],
		't.sinensis': [1, 0, 2]}) #will need to make this a .csv


	def __init__(self, seq = default_seq, mat = default_mat):
		self.seq = seq #this can be .fasta or .csv
		self.mat = mat #this needs to be .csv
		# Include a parameter so either both are given, or both are left blank. Otherwise, an error

	def __repr__(self):
		return f"Phylogenetic diversity will be calculated using sequences in {self.seq} and communities in {self.mat}."

	def csv_to_fasta(self):
		"""
		A function to pull GenBank sequences from accession numbers if self.seq is a .csv
		"""

	def align(self):
		"""
		A function to produce a file of aligned sequences from MUSCLE.
		Takes a .fasta file (either given, or created in the previous function).
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







