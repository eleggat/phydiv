# phydiv
## Phylogenetic diversity metrics from community data

This package calculates phylogenetic diversity metrics from community occurence data, and can visualize communities on their metacommunity tree. It also has functionality to simulate community occurence data under specified assumptions of phylogenetic structure. This package utilizes the `toytree` package for tree construction and visualization.

**Input:**
A metacommunity tree (Newick, NHX, or Nexus format), and community occurence data in the form of a site by species matrix (CSV). Built-in data is available for users to test the package without their own input data.

If using the data simulation functionality: the size of the metacommunity species pool, phylogenetic structure assumption (null, more related, less related), and the species richness of the simulated communities.

**Output:** 
Metrics of phylogenetic diversity (Faith's PD, MPD, and MNTD) for each community, and plotting options for community phylogeny visualization.

### Installation
`conda install toytree phydiv -c conda-forge`

```
git clone https://github.com/eleggat/phydiv.git
cd ./phydiv
pip install -e .
```

### Usage
The three functionalities of `phydiv` are: `metric`, `plot`, and `simpd`. Help pages for each can be accessed as follows:
```
python phydiv metric -h
python phydiv plot -h
python phydiv simpd -h
```

#### `metric`
|Argument|Description|
|--------|-----------|
|`tree`|The metacommunity tree (Newick, NHX, or Nexus format). **Must be specified if `matrix` is specified**. If left blank, built-in data will be used.|
|`matrix`|A site by species matrix for species occurrence data in each community (CSV format). **Must be specified if `tree` is specified**. If left blank, built-in data will be used.|
|`diversity`|The diversity metric(s) to be calculated. Options are Faith's PD, MPD, MNTD, or all three. *Default `all`*.|
|`file`|**Required**. File name of csv for saving metric(s).|


#### `plot`
|Argument|Description|
|--------|-----------|
|`tree`|The metacommunity tree (Newick, NHX, or Nexus format). **Must be specified if `matrix` is specified**. If left blank, built-in data will be used.|
|`matrix`|A site by species matrix for species occurrence data in each community (CSV format). **Must be specified if `tree` is specified**. If left blank, built-in data will be used.|
|`plottype`|Specify type of plot to use for community occurrence visualization. Options are: `prune`, which prunes the metacommunity tree to the specified community; `highlight`, which highlights tips on the metacommunity for species occurring in the specified community; or `all`, which plots a heatmap of all communities onto the metacommunity tree, with each column representing a community and each row representing a species. *Default `all`*.|
|`community`|Selected community to plot for `highlight` and `prune` plot types. Required for `highlight` and `prune`, optional for `all`.|
|`file`|**Required**. File name for saving plot. Should be HTML, SVG, PNG, or PDF.|


#### simpd
|Argument|Description|
|--------|-----------|
|`ntips`|Number of tips in the metacommunity phylogeny (number of species). *Default 100*.|
|`sr`|Species richness of the simulated community. Must be < `ntips`. **Required**.|
|`pa`|Phylogenetic assumption of the community simulation. -1: related species are least likely to co-occur; 0: no phylogenetic structure; 1: related species are most likely to co-occur. *Default 0*.|
|`nsites`|Number of sites (rows) to simulate for the site by species matrix. *Default 10*.|
|`treefile`|File name for saving tree data. Should be Newick. **Required**.|
|`communityfile`|File name for saving community matrix. Should be CSV. **Required**.|


**Bash example:**
```
# Simulating data for diversity metrics and plotting
python phydiv simpd --ntips 50 --sr 15 --pa 0.7 --treefile my_tree.nwk --communityfile my_comm.csv

# Calculating all diversity metrics
python phydiv metric --tree my_tree.nwk --matrix my_comm.csv --diversity all --file metrics.csv

# Plotting all communities on a heatmap
python phydiv plot --tree my_tree.nwk --matrix my_comm.csv --plottype all --file plot.png

```

**Jupyter notebook example:**
```
import phydiv

my_community = phydiv.Phydiv(tree = my_tree.nwk, matrix = my_comm.csv)
my_community.plot_all() # plots to stdout
my_community.metric_all(csv = "my_metrics.csv")
```


### See also
- [`toytree`](https://github.com/eaton-lab/toytree): A package for plotting and querying phylogenetic trees
- [`picante`](https://github.com/skembel/picante): A phylogenetic diversity package for R
- Vellend, M., Cornwell, W. K., Magnuson-Ford, K. & Mooers, A. Ø. [Measuring phylogenetic biodiversity.](http://balsas-nahuatl.org/barcoding-electronic-docs/Vellend-et-al_Measuring-phylogenetic-diversity_2011_bookchap%5B1%5D.pdf) in Biological Diversity: Frontiers in Measurement and Assessment (eds. Magurran, A. E. & McGill, B. J.) (Oxford University Press, 2011).
