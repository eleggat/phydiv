# phydiv
## Pylogenetic diversity metrics from community sequence data
This package takes community sequence data to calculate metrics of phylogenetic diversity. The communities sequences may be input by the user as a .fasta file, or may be given as a .csv file containing GenBank accession numbers. Species may also by removed prior to calculation if specified by the user. This may be useful for comparing results to other diversity metrics that use different species lists. Available metrics to calculate include Fisher's index (FI), mean phylogenetic distance (MPD), and abundance-weighted mean phylogenetic distance (MPDaw).

**Input:**
1. A .fasta file containing community sequences, or a .csv file containing GenBank accession numbers, and
2. a site by species matrix for the communities of interest.

If using accession numbers, the .csv should be two columns, with species name or ID in the first and accession number in the second. The format of the species names/IDs does not matter, but should be consistent.
*Example .csv:*
|Species id|Accession number|
|----------|----------------|
|c.glandium|KC784066.1|
|d.plexippus|GU672935.1|
|t.sinensis|MZ099432.1|

*Example matrix:*
|Site|c.glandium|d.plexippus|t.sinensis|
|----|----------|-----------|----------|
|site1|10|5|1|
|site2|6|0|0|
|site3|2|8|2|

*Additional specifications:*
- Species may be removed from the communities prior to metric calculation using an optional specification by the user.

**Output:** 
1. A .csv file containing specified community phylogentic diversity metrics (*Default: only FI*).
2. Optional: a metacommunity phylogenetic tree.
3. Optional: phylogenetic trees with highlighted tips for each community.
*Example .csv:*
|Site|FI|
|----|--|
|site1|TBD|
|site2|TBD|
|site3|TBD|


### In development

#### Installation
```
conda install toytree phydiv -c conda-forge
git clone https://github.com/eleggat/phydiv.git
cd ./phydiv
pip install -e .
```





