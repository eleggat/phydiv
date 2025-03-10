#!/usr/bin/env python

"""
A function for simulating site by species matrices under different assumptions of phylogenetic diversity
"""

# Imports
import numpy as np
import toytree

# Functions


## Function to select species from the tree

#this function will be editable by the user
#can change phylogenetic relatedness of the community (0 = species are least likely to occur with relatives, 1 = species are most likely to appear with relatives)
#will only be presence/absence, not abundance-weighted

def sp_select():
	"""
	Creates a community matrix from a species pool according to different assumtions of phylogenetic diversity

	Parameters:
	---
	pa: float between -1 to 1
		- -1 = related species are least likely to co-occur
		- 1 = related species are most likely to co-occur
		- 0 = no phylogenetic structure

	Return:
	---
	

	"""

	#Creating the species pool (100 species)
	sp_tree = toytree.rtree.baltree(100, random_names=False) #create the tree
	species = sp_tree.get_tip_labels() #list of species in the pool


## Function to simulate species selection for many sites with same number of species

#this function will be editable by the user
#can change number of simulations



## Function to simulate species selection from sites with increasing number of species









