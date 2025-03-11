#!/usr/bin/env python

"""
A class that allows users to make site by species matrices from a random metacommunity species pool with customizable phylogenetic assumptions
"""

# Imports
import numpy as np
import toytree

# Establishing the class
class Simpd
	def __init__(self, ntips = 100):
		self.ntips = ntips

		self.sp_tree = toytree.rtree.baltree(ntips, random_names = False) #the metacomunity tree
		self.species = sp_tree.get_tip_labels() #list of species in the metacommunity

	def __repr__(self):
		return f"This metacommunity has {ntips} species."



	def simcom(sr, pa = 0.5, verbose = False):
    """
    Simulate one community from the species pool under different phylogenetic structure assumptions

    Parameters:
    ---
    sr: int; species richness
        - Must be int < len(species)
    pa: float (-1 to 1); phylogenetic assumption
        - -1 = related species are least likely to co-occur
        - 0 = no phylogenetic structure
        - 1 = related species are most likely to co-occur

    Return:
    ---
    Matrix of species presence/absence
    
    """



    def simmatrix(sr, pa = 0.5, nsites, verbose = False):
    """
    Simulate multiple communities from the species pool under the same phylogenetic structure assumption

    Parameters:
    ---
    sr: int; species richness
        - Must be int < len(species)
    pa: float (-1 to 1); phylogenetic assumption
        - -1 = related species are least likely to co-occur
        - 0 = no phylogenetic structure
        - 1 = related species are most likely to co-occur
    nsites: int; number of sites (rows) in the resulting matrix

    Return:
    ---
    Matrix of species presence/absence at each site

    """




    def simsr(sr_min, sr_max, pa = 0.5, verbose = False):
    """
    Simulate multiple communities from the species pool of increasing species richness under the same phylogenetic structure assumption

    Parameters:
    ---
    sr_min: int; species richness
        - Must be int < len(species)
    sr_max: int; species richness
        - Must be int < len(species)
        - Must be int > sr_min
    pa: float (-1 to 1); phylogenetic assumption
        - -1 = related species are least likely to co-occur
        - 0 = no phylogenetic structure
        - 1 = related species are most likely to co-occur

    Return:
    ---
    Matrix of species presence/absence at each site
    """



	## Function to simulate species selection from sites with increasing number of species









