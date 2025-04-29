# phydiv
## Phylogenetic diversity metrics from community data

This package calculates phylogenetic diversity metrics from community occurence data, and can visualize communities on their metacommunity tree. It also has functionality to simulate community occurence data under specified assumptions of phylogenetic structure. This package utilizes the `toytree` package for tree construction and visualization.

**Input:**
A metacommunity tree (Newick, NHX, or Nexus format), and community occurence data in the form of a site by species matrix (CSV).

If using the data simulation functionality: the size of the metacommunity species pool, phylogenetic structure assumption (null, more related, less related), and the species richness of the simulated communities.

**Output:** 
Metrics of phylogenetic diversity (Faith's PD, MPD, and MNTD) for each community, and plotting options for community phylogeny visualization.

### Installation
`conda install toytree phydiv -c conda-forge`

```
git clone https://github.com/eleggat/phydiv.git
cd ./mini-project
pip install -e .
```

### Usage
|Argument|Description|
|--------|-----------|
|`tree`|The metacommunity tree (Newick, NHX, or Nexus format). **Must be specified if `matrix` is specified**. If left blank, built-in data will be used.|
|`matrix`|A site by species matrix for species occurrence data in each community (CSV format). **Must be specified if `tree` is specified**. If left blank, built-in data will be used.|
|`plot`|*Optional*. Specify type of plot to use for community occurrence visualization. Options are: `prune`, which prunes the metacommunity tree to the specified community; `highlight`, which highlights tips on the metacommunity for species occurring in the specified community; or `all`, which plots a heatmap of all communities onto the metacommunity tree, with each column representing a community and each row representing a species.|
|`diversity`|*Optional*. Calculates all phylogenetic diversity metrics for each community. Output is written to a CSV file with given str name.|

**Bash example:**
```
python phydiv --tree my_tree.nwk --matrix my_matrix.csv --plot all --diversity my_metrics.csv
```

**Jupyter notebook example:**
```
import phydiv

my_community = Phydiv(tree = my_tree.nwk, matrix = my_matrix.nwk)
my_community.plot_all()
my_community.metric_all(csv = "my_metrics.csv")
```


### Simpd
`Phydiv` includes a built-in data simulation tool, `Simpd`, which simulates site by species matrices under different assumptions of phylogenetic diversity for a mock community.

**Input:**
The size of the metacommunity species pool, diversity assumption (null, more related, less related), and the species richness of the simulated communities.

**Output:** 
A site by species matrix under the specified assumption of phylogenetic diversity.

#### Usage
|Argument|Description|
|--------|-----------|
|`ntips`|Number of tips in the metacommunity phylogeny (number of species). *Default 100*.|
|`sr`|Species richness of the simulated community. Has no default value and **must be specified**. sr must be < ntips.|
|`pa`|Phylogenetic assumption of the community simulation. -1: related species are least likely to co-occur; 0: no phylogenetic structure; 1: related species are most likely to co-occur. *Default 0*.|
|`nsites`|Number of sites (rows) to simulate for the site by species matrix. *Default 10*.|
|`df`|Community simulation output is a numpy array when False. Output is a numpy array when True. *Default False*.|
|`csv`|When given, output is written to a CSV file with specified str name.|

**Bash example:**
```
python phydiv simpd --sr 25 --pa 0.7 --nsites 30 --csv site_sp_matrix.csv
```

**Jupyter notebook example:**
```
import phydiv

simulation = Simpd().simmat(sr = 25, pa = 0.7, nsites = 30, df = True)
```

### See also
- [`toytree`](https://github.com/eaton-lab/toytree): A package for plotting and querying phylogenetic trees
- [`picante`](https://github.com/skembel/picante): A phylogenetic diversity package for R
- Vellend, M., Cornwell, W. K., Magnuson-Ford, K. & Mooers, A. Ø. [Measuring phylogenetic biodiversity.](http://balsas-nahuatl.org/barcoding-electronic-docs/Vellend-et-al_Measuring-phylogenetic-diversity_2011_bookchap%5B1%5D.pdf) in Biological Diversity: Frontiers in Measurement and Assessment (eds. Magurran, A. E. & McGill, B. J.) (Oxford University Press, 2011).
