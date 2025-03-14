# simpd
## Site by species matrix simulations from diversity assumptions

This package simulates site by species matrices under different assumptions of phylogenetic diversity for a mock community.

**Input:**
The size of the metacommunity species pool, diversity assumption (null, more related, less related), and the species richness of the simulated communities

**Output:** 
A site by species matrix under the specified assumption of phylogenetic diversity.

### Installation
`conda install toytree simpd -c conda-forge`

```
git clone https://github.com/eleggat/mini-project.git
cd ./mini-project
pip install -e .
```
### Usage
|Argument|Description|
|--------|-----------|
|`ntips`|Number of tips in the metacommunity phylogeny (number of species). *Default 100*.|
|`sr`|Species richness of the simulated community. Has no default value and **must be specified**. sr must be < ntips.|
|`pa`|Phylogenetic assumption of the community simulation. -1: related species are least likely to co-occur; 0: no phylogenetic structure; 1: related species are most likely to co-occur. *Default 0*.|
|`nsites`|Number of sites (rows) to simulate for the site by species matrix. *Default 10*.|
|`df`|Community simulation output is a numpy array when False. Output is a numpy array when True. *Default False*.|
|`csv`|When given, output is written to a csv file with specified str name. Do not include .csv extension in file name.|

**Bash example:**
```
python simpd --sr 25 --pa 0.7 --nsites 30 --csv site_sp_matrix
```

**Jupyter notebook example:**
```
import simpd

simulation = Simpd()
simulation.simmat(sr = 25, pa = 0.7, nsites = 30, df = True)
```