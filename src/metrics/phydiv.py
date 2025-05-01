#!/usr/bin/env python

"""
A program that takes a metacommunity phylogeny and site by species matrices to
visualize community phylogenetic assembly and calculate phylogenetic diversity
"""

# Imports
import itertools
import os

import numpy as np
import pandas as pd

import toytree
import toyplot


# Establishing the main Phydiv class
class Phydiv:
    """
    This class takes a metacommunity tree and site by species matrix to
    produce measures of phylogenetic diversity and tree visualizations.
    """

    # Initial setup functions

    def __init__(self, tree = None, matrix = None):
        # Default data
        script_dir = os.path.dirname(__file__)
        matrix_path = os.path.join(script_dir, 'data', 'mock_matrix.csv')
        tree_path = os.path.join(script_dir, 'data', 'mock_tree.nwk')

        default_tree = toytree.tree(tree_path)
        default_matrix = pd.read_csv(matrix_path)

        if (tree is None) != (matrix is None):
            raise ValueError("You must provide both 'tree' and 'matrix', or neither.")
        elif tree is not None and matrix is not None: #user input
            self.tree = toytree.tree(tree)
            self.matrix = pd.read_csv(matrix, index_col = 0)
            self.matrix.columns = self.matrix.columns.str.replace(' ','_') #get rid of spaces in spp names
            self.matrix = self.matrix.dropna() #drop NaNs in matrix
        else: #default data
            self.tree = default_tree
            self.matrix = default_matrix

    	# List of species in each community
        self.spp = self.matrix.apply(lambda row: row.index[row > 0].tolist(), axis=1)


    def __repr__(self):
        return f"Phylogenetic diversity will be calculated using the metacommunity tree {self.tree} and communities in {self.matrix}."


    # Plotting functions

    def plot_tree(self):
        """
        Plot the whole metacommunity

        Return:
        ---
        plot of the metacommunity phylogeny
        """
        self.tree.draw();

    def plot_prune(self, community = None, save = None):
        """
        Plot pruned trees for sample communities

        Parameters:
        ---
        community: list of communities to plot, given as matrix row indices

        Return:
        ---
        plot of communities pruned from metacommunity phylogeny
        """
        if type(community) is int:
            pass
        elif type(community) is not list:
            raise TypeError("Communities for plotting should be given as a list of row indices")
        elif not community:
            community = range(len(self.matrix)) #all communities if none specified

        # creating a tree for each mock community
        comm_trees = []
        for i in range(len(self.spp)):
            query_list = self.spp[i]
            new_tree = toytree.mod.prune(self.tree, *query_list)
            comm_trees.append(new_tree)

        # plotting only specified communities (default: plot all)
        if type(community) is int:
            comm_trees[community].draw(); #.label.text(f"community {community}")

        else:
            mtree = toytree.mtree([comm_trees[c] for c in community])
            canvas, axes, marks = mtree.draw();
            # add a label to each subplot
            #for adx, ax in enumerate(axes):
            #    ax.label.text = f"community {comm_trees[c]}"

        if type(save) is str:
        	toytree.save(canvas, f"{save}")


    def plot_highlight(self, community = None, abundance = False, save = None):
        """
        Plot metacommunity phylogeny with tips highlighted for species in specified communities

        Parameters:
        ---
        community: list of communities to plot, given as matrix row indices

        Return:
        ---
        plot of metacommunity phylogeny with highlighted tips
        """

        if type(community) is int:
            pass
        #elif type(community) is not list:
        #    raise Exception("Communities for plotting should be given as a list of row indices")
        #elif not community:
        #    community = range(len(matrix)) #all communities if none specified
        else:
            raise TypeError("Specify community by matrix row index")

        # make species matrix a numpy array
        matrix_np = self.matrix.to_numpy()

        # convert all data to 1s and 0s if abundance is False
        nrows = matrix_np.shape[0]
        ncols = matrix_np.shape[1]
        if not abundance:
            for r in range(nrows):
                for c in range(ncols):
                    if matrix_np[r][c] > 0:
                        matrix_np[r][c] = 1
                    else:
                        matrix_np[r][c] = 0

        #create a mask for species in the community only
        mask = []
        for i in range(len(self.spp)):
            query_list = self.spp[i]
            comm_mask = self.tree.get_node_mask(*query_list)
            mask.append(comm_mask)

        # set abundance data for nodes if abundance is True
        #if abundance:
        #    self.tree.set_node_data("abundance", matrix_np[community], inplace = True)

        # plotting community
        #colormap = toyplot.color.brewer.map("RedPurple")

        self.tree.draw(node_mask=mask[community], node_sizes=12);

        if type(save) is str:
        	toytree.save(canvas, f"{save}")


    def plot_all(self, abundance = False, save = None):
        """
        Plot metacommunity phylogeny with heatmap for species presence across all communities

        Parameters:
        ---

        Return:
        ---
        plot of metacommunity phylogeny with heatmap of species for all communities, colored by presence/absence or abundance
        """

        # make species matrix a numpy array
        matrix_np = self.matrix.to_numpy()

        # set row/column parameters
        tmatrix = np.transpose(matrix_np) #transpose matrix to match vertical tree
        trows = tmatrix.shape[0]
        tcolumns = tmatrix.shape[1]

        # convert all data to 1s and 0s if abundance is False
        if not abundance:
            for r in range(trows):
                for c in range(tcolumns):
                    if tmatrix[r][c] > 0:
                        tmatrix[r][c] = 1
                    else:
                        tmatrix[r][c] = 0

        # create a canvas
        c_width = tcolumns*25 + 50 #total width
        c_height = trows*15 + 50 #total height
        canvas = toyplot.Canvas(width=c_width, height=c_height);

        # add tree 
        tree_xmin = 25
        tree_xmax = 125
        tree_ymin = 25
        tree_ymax = c_height - 25
        axes = canvas.cartesian(bounds=(tree_xmin, tree_xmax, tree_ymin, tree_ymax))
        self.tree.draw(axes=axes, tip_labels=True, tip_labels_align=True)

        # add matrix
        tab_xmin = tree_xmax + 5
        tab_xmax = c_width - 25
        tab_ymin = tree_ymin
        tab_ymax = tree_ymax
        table = canvas.table(
            rows= trows, #n species
            columns= tcolumns,  #n communities
            margin=1,
            bounds=(tab_xmin, tab_xmax, tab_ymin, tab_ymax),
        )

        colormap = toyplot.color.brewer.map("RedPurple") #need to reverse color!

        # apply a color to each cell in the table
        for ridx in range(trows): #row index
            for cidx in range(tcolumns): #column index
                cell = table.cells.cell[ridx, cidx]
                cell.style = {
                    "fill": colormap.colors(tmatrix[ridx, cidx], 0, np.max(tmatrix)),
                }

        # style the gaps between cells
        table.body.gaps.columns[:] = 3
        table.body.gaps.rows[:] = 3

        # hide axes coordinates
        axes.show = False

        if type(save) is str:
        	toytree.save(canvas, f"{save}")


    # Metric functions

    def metric_fpd(self, csv = None):
        """
        Calculate Faith's phylogenetic diversity (FPD or PD) for each community
        Here, abbreviated as FPD to reduce confusion with pandas as pd

        Parameters:
        ---
        csv: str to write results to csv file. Results are printed to stdout by default. Optional.

        Return:
        ---
        Numpy array of FPD values for each community. Option for writing to csv.
        """

        # creating a tree for each mock community
        comm_trees = []
        for i in range(len(self.spp)):
            query_list = self.spp[i]
            if len(query_list) == 0:
                new_tree = None #no tree if no species
            else:
                new_tree = toytree.mod.prune(self.tree, *query_list)
            comm_trees.append(new_tree)

        # For the pruned trees, sum distances
        tree_fpd = []
        for ptree in comm_trees:
            if ptree == None:
                fpd = None #no fpd if no species/tree
            else:
                fpd = ptree.get_node_data("dist").sum()
            tree_fpd.append(fpd)

        # Option to write csv or print to stdout
        if type(csv) is str:
            pd.DataFrame(tree_fpd).to_csv(f"{csv}", index = False) #write the csv if specified
        else:
            return tree_fpd

    def metric_mpd(self, abundance = False, csv = None):
        """
        Calculate mean phylogenetic distance (MPD) for each community

        Parameters:
        ---
        csv: str to write results to csv file. Results are printed to stdout by default. Optional.

        Return:
        ---
        Numpy array of MPD values for each community. Option for writing to csv.
        """

        # calculate MPD for each community
        tree_mpd = []
        for i in range(len(self.spp)):
            pairs = list(itertools.combinations(self.spp[i], 2))
            pair_dists = []
            for p in range(len(pairs)):
                query_list = pairs[p]
                dist = self.tree.distance.get_node_distance(*query_list)
                pair_dists.append(dist)
            if len(pair_dists) == 0:
                tree_mpd.append(None) #append none if len = 0
            else:
                tree_mpd.append(sum(pair_dists)/len(pair_dists)) #append average to mpd list

        # Option to write csv or print to stdout
        if type(csv) is str:
            pd.DataFrame(tree_mpd).to_csv(f"{csv}", index = False) #write the csv if specified
        else:
            return tree_mpd

    def metric_mntd(self, abundance = False, csv = None):
        """
        Calculate mean nearest taxon distance (MNTD) for each community

        Parameters:
        ---
        csv: str to write results to csv file. Results are printed to stdout by default. Optional.

        Return:
        ---
        Numpy array of MNTD values for each community. Option for writing to csv.
        """

        # get distance matrix of metacommunity tree
        meta_dm = self.tree.distance.get_tip_distance_matrix(df = True)

        #remove absent species from distance matrix for each community
        comm_dists = []
        for comm in self.spp:
            comm_dm = meta_dm.loc[comm, comm]
            comm_dists.append(comm_dm)

        # calculate MNTD for each community
        tree_mntd = []
        for dm in comm_dists: #for community in dms of communities list
            nt = [] #empty list of nearest taxa
            for row in range(dm.shape[0]): #for each species (row)
                sp_dist = list(dm.iloc[row]) #select species row
                del sp_dist[row] #exclude same-species distance
                if len(sp_dist) == 0:
                    pass #do nothing if sp_dist is empty
                else:
                    nt.append(min(sp_dist)) #append minimum to nearest list
            if len(nt) == 0:
                tree_mntd.append(None) #append none if len = 0
            else:
                tree_mntd.append(sum(nt)/len(nt)) #append average to mntd list

        # Option to write csv or print to stdout
        if type(csv) is str:
            pd.DataFrame(tree_mntd).to_csv(f"{csv}", index = False) #write the csv if specified
        else:
            return tree_mntd


    def metric_all(self, csv = None):
        """
        Calculate all phylogenetic diversity metrics for each community (Faith's PD, MPD, and MNTD)

        Parameters:
        ---
        tree: toytree tree
        matrix: site by species matrix in pandas format

        Return:
        ---
        Pandas dataframe of diversity metric values for each community. Option for writing to csv.
        """

        # calculate all metrics
        fpd = self.metric_fpd()
        mpd = self.metric_mpd()
        mntd = self.metric_mntd()

        #combine all metrics into pandas dataframe
        metrics = pd.DataFrame({"Faith's PD": fpd,
                                "MPD": mpd,
                                "MNTD": mntd})

        # Option to write csv or print to stdout
        if type(csv) is str:
            metrics.to_csv(f"{csv}", index = False) #write the csv if specified
        else:
            return metrics






