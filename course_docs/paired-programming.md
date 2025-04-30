## Goal of the project: Is it clear to you from the proposal.md how the goal can be accomplished using Python and the specified packages?

The overall goal of the project is made clear, which is to calculate phylogenetic diversity metrics from community sequence data. The proposal explains what the usage of the package is, which diversity metrics will be available (MPD, MPDaw, and FPD), what inputs are necessary, and what the outputs will be. The packages that are used are written within the installation code, but could be expanded on to be made more clear what packages they will be able to use if they are just copy-pasting the installation code and not paying as close attention. 

## The Data: Is it clear to you from the proposal.md what the data for this project is, or will look like?

The data requirements are listed clearly. The user will need to provide either a .fasta file of sequences of OTUs, or a .csv file with GenBank accession numbers, and they will also provide a site-by-OTU matrix. The examples provided make it clear what needs to be provided. What could be a bit more clear would be how the program will handle GenBank numbers instead of sequences, given they are so different, and whether one is better than the other. Maybe this is more clear to those in this field, but does the structure of the program prefer one or the other, or does it truly not matter which you choose? The output will be a .csv file containing specified community phylogentic diversity metrics, and you can optionally retrieve a visualized metacommunity phylogenetic tree or a visualized phylogenetic tree with highlighted tips for each community.  

## The code: (Look at the Python code files in detail first and try to comprehend a bit of what is written so far)


### Does the current code include a proper skeleton (pseudocode) for starting this project?

Yes, the current code has a strong skeleton structure for starting the project. It lists all of the functions that will eventually be defined with code. There are also comments that make it clear what will need to be entered in later on to make this code function, including the need for error messages, etc. 

### What can this code do so far?

At this point, the code in `phydiv.py` is mostly a skeleton, but it sets up the `Phydiv` class, imports all of the necessary tools for running this package, and defines a function `repr()` that prints a statement about what data will be used in this run of the package. 

### Given the project description, what are some individual functions that could be written to accomplish parts of this goal?

To accomplish parts of this goal, there are already many functions that have been named and just need to be filled out. These include `csv_to_fasta()`, a function to pull GenBank sequences from accession numbers if self.seq is a .csv, `align()`, a function to produce a file of aligned sequences from MUSCLE, and takes a .fasta file (pass in from previous function), `metacomm()`, a function to make a metacommunity tree from the sequences, `comm()`, a function that selects present species from the tree for each community, `mpd()`, a function to calculate MPD for each community and return a matrix of community and values, `mpdaw()`, a function to calculate MPDaw for each community and return a matrix of community and values, and `faith()`, and a function to calculate Faith's PD for each community and return a matrix of community and values. These outlined functions will be very useful for implementing the goal of the package. Additionally, I suggested adding `def main()` to set up the argparse functions for using the command line interface. 

### Code contributions/ideas: See description below for what to write here.

Added the following to allow for running in the command-line:
`if __name__ == "__main__":
    main()`

Also added the following to setup a function for argparse:
`def main():
    """
    Main function to process arguments and call the appropriate function.
    """`

## Other comments

Just fixed typo in title for "phylogentic"! I might also use "site-by-matrix" instead of "site by matrix" to make it clear what the structure needs to be. To make the intro a bit more accessible, I might write out "OTU" in full before using the acronym as well.