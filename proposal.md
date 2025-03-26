# phydiv
## Pylogenetic diversity metrics from community sequence data
This package takes community sequence data to calculate metrics of phylogenetic diversity. The community sequences may be input by the user as a `.fasta` file, or may be given as a `.csv` file containing GenBank accession numbers. OTUs may also by removed prior to calculation if specified by the user. This may be useful for comparing results to other diversity metrics that use different OTU/species lists. Available metrics to calculate include mean phylogenetic distance (MPD), abundance-weighted mean phylogenetic distance (MPDaw), and Faith's phylogenetic diversity (FPD).

**Input:**
1. A `.fasta` file containing sequences for each OTU, or a `.csv` file containing GenBank accession numbers, **and**
2. a site by OTU matrix for the communities of interest.
3. Optional: OTUs may be removed from the communities prior to metric calculation with a user specification

If using accession numbers, the `.csv` should be two columns, with OTU name or ID in the first and accession number in the second. The format of the OTU names/IDs does not matter, but should be consistent.


*Example `.csv`:*
|OTU id|Accession number|
|----------|----------------|
|c.glandium|KC784066.1|
|d.plexippus|GU672935.1|
|t.sinensis|MZ099432.1|

*Example matrix:*
|Community|c.glandium|d.plexippus|t.sinensis|
|----|----------|-----------|----------|
|site1|10|5|1|
|site2|6|0|0|
|site3|2|8|2|


**Output:** 
1. A `.csv` file containing specified community phylogentic diversity metrics (*Default: only MPD*).
2. Optional: a visualiized metacommunity phylogenetic tree.
3. Optional: visualized phylogenetic trees with highlighted tips for each community.


*Example `.csv`:*
|Site|MPD|
|----|--|
|site1|TBD|
|site2|TBD|
|site3|TBD|


The above mock community data is built into the package, and the output can be replicated by leaving both the OTU file and community matrix fields blank.


### In development

#### Installation
```
conda install toytree Bio.Align.Applications.MuscleCommandline phydiv -c conda-forge
git clone https://github.com/eleggat/phydiv.git
cd ./phydiv
pip install -e .
```

### Resources
- [`picante`](https://github.com/skembel/picante): A phylogenetic diversity package for R
- Vellend, M., Cornwell, W. K., Magnuson-Ford, K. & Mooers, A. Ø. [Measuring phylogenetic biodiversity.](http://balsas-nahuatl.org/barcoding-electronic-docs/Vellend-et-al_Measuring-phylogenetic-diversity_2011_bookchap%5B1%5D.pdf) in Biological Diversity: Frontiers in Measurement and Assessment (eds. Magurran, A. E. & McGill, B. J.) (Oxford University Press, 2011).
- [NCBI nucleotide database](https://www.ncbi.nlm.nih.gov/nucleotide/) for accession numbers
- [MUSCLE sequence alignment](https://www.ebi.ac.uk/jdispatcher/msa/muscle?stype=protein) (built into `phydiv`)




