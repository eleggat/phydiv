#!/usr/bin/env python

"""
A class that allows users to make site by species matrices from a random metacommunity species pool with customizable phylogenetic assumptions
"""

# Imports
import numpy as np
import pandas as pd
import toytree

# Establishing the class
class Simpd:
    """
    This class creates a balanced phylogeny that can be used for community simulations
    """
    def __init__(self, ntips = 100):
        self.ntips = ntips

        self.sp_tree = toytree.rtree.baltree(ntips, random_names = False) #the metacomunity tree
        self.species = self.sp_tree.get_tip_labels() #list of species in the metacommunity

    def __repr__(self):
        return f"This metacommunity has {self.ntips} species."
    
    def simcom(self, sr, pa = 0, df = True, verbose = False):
        """
        Simulate a community from the species pool under different phylogenetic structure assumptions
        
        Parameters:
        ---
        sr: int; species richness
            - Must be int < len(species)
        pa: float (-1 to 1); phylogenetic assumption (default = 0)
            - -1 = related species are least likely to co-occur
            - 0 = no phylogenetic structure
            - 1 = related species are most likely to co-occur
        
        Return:
        ---
        matrix of species presence/absence
        """
        
        #Get species distance matrix
        dm = self.sp_tree.distance.get_tip_distance_matrix(df = True)
        
        #Start community with a random species
        comm = []
        start = np.random.choice(dm.index)
        comm.append(start)
        if verbose:
            print(f"The starting species is {comm}")
        
        #Making a list of unselected species
        unused = set(dm.index)
        unused.remove(start)
        
        #Creating probability weights (min and max are 0.5 for pa = 0)
        max_p = abs(pa)/2 + 0.5
        min_p = 1 - max_p
        if verbose:
            print(f"min = {min_p}, max = {max_p}")
        
        #Select species from the distance matrix
        for sp in range((sr - 1)):
            #stop if no more species remain
            if not unused:
                raise Exception("Species richness must be less than or equal to the species pool.")
                break
            
            #get distances for current species
            current_sp = comm[-1]
            sp_dists = dm.loc[current_sp].copy()
            
            #setting already selected species distances to zero
            for name in dm.index:
                if name not in unused:
                    sp_dists[name] = 0
                    
            #finding min and max distances
            d_min, d_max = sp_dists.min(), sp_dists.max()
            if verbose:
                print(f"The min distance = {d_min}, and the max distance = {d_max}")
            
            #apply weighted probabilities to distances
            if sp_dists.sum() > 0: #ensure there are species left to collect
                if pa > 0: #smaller distances more likely
                    probabilities = sp_dists.map(lambda x: 0 if x == 0 else max_p - (x - d_min) * (max_p - min_p) / (d_max - d_min))
                elif pa == 0: #no phylogenetic structure
                    probabilities = sp_dists.map(lambda x: 0 if x == 0 else 0.5)
                elif pa < 0: #greater distances more likely
                    probabilities = sp_dists.map(lambda x: 0 if x == 0 else min_p + (x - d_min) * (max_p - min_p) / (d_max - d_min))
                
                #choose one of the species distance groups
                prob_uniq = probabilities.unique() #unique probabilities
                if pa != 0:
                    prob_scale = []
                    for p in prob_uniq:
                        new_prob = p / sum(prob_uniq) #scale probabilities so they sum to 1
                        prob_scale.append(new_prob)
                    next_sp_prob = np.random.choice(prob_uniq, p = prob_scale) #pick a probability group by scaled probability
                else:
                    next_sp_prob = 0.5
                if verbose:
                    print(f"The next species probability is {next_sp_prob}")
                    print(probabilities)
                
                #selecting the next species from the corresponding probability group
                possible_sp = probabilities[probabilities == next_sp_prob]
                next_sp = np.random.choice(possible_sp.index)
                if verbose:
                    print(f"The next species is {next_sp}")
                
                #add next species and remove it from list of possible species
                comm.append(next_sp)
                unused.remove(next_sp)
            
            else:
                print("No more species!")
                break
        if verbose:
            print(comm)
        
        #Creating the presence/absence matrix
        comm_pa_list = []
        for sp in self.species:
            if sp in comm:
                comm_pa_list.append(1)
            else:
                comm_pa_list.append(0)
        if verbose:
            print(comm_pa_list)
        comm_pa = pd.DataFrame([comm_pa_list], columns = self.species)
        
        if not df:
            comm_pa = comm_pa.to_numpy()
        
        return comm_pa
    
    
    def simmat(self, sr, pa = 0, nsites = 10, df = True):
        """
        Simulate a site by species matrix under a specified phylogenetic assumption
        
        Parameters:
        ---
        nsites: int; number of rows (sites)
        sr: int; species richness
            - Must be int < len(species)
        pa: float (-1 to 1); phylogenetic assumption (default = 0)
            - -1 = related species are least likely to co-occur
            - 0 = no phylogenetic structure
            - 1 = related species are most likely to co-occur
        
        Return:
        ---
        matrix of species presence/absence; rows = sites, columns = species (pandas df default)
        """
        ssm = pd.DataFrame([], columns = self.species) #make an empty dataframe with species as columns
        for s in range(nsites):
            site = self.simcom(sr, pa)
            ssm = pd.concat([ssm, site], ignore_index = True) #add new community row to dataframe
        
        if not df:
            ssm = ssm.to_numpy() #changes pandas data frame output to numpy array
        
        return ssm
    


    