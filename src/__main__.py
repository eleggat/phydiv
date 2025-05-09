#!/usr/bin/env python

"""
Main argparse for command line
"""

# Imports
import argparse
from metrics.phydiv import Phydiv
from simpd.simpd import Simpd

# Arparser
def parse_command_line():
	"parses args for the whole phydiv module"

	# init parser and add arguments
	parser = argparse.ArgumentParser()

	# add subparser for using phydiv functions and simpd separately
	subparser = parser.add_subparsers(dest = "command", required = False)




	# plotting subcommand
	plot_parser = subparser.add_parser("plot", help = "Plot community trees.")

	# add long args
	plot_parser.add_argument(
		"-t",
		"--tree",
		help="Metacommunity tree. Should be Newick, NHX, or Nexus format. If given, --matrix must also be given.",
		dest='tree', type=str, default='metrics/data/mock_tree.nwk')

	plot_parser.add_argument(
		"-m",
		"--matrix",
		help="Site-by-OTU matrix of communities. Must be a CSV. If given, --tree must also be given.",
		dest='matrix', type=str, default='metrics/data/mock_matrix.csv')

	plot_parser.add_argument(
		"-p",
		"--plottype",
		help="Type of plot. Options: plot all communities on metacommunity phylogeny as a heatmap ('all'); plot metacommunity phylogeny with tips highlighted for one community ('highlight'); plot pruned trees for up to four communities ('prune').",
		choices=["all", "highlight", "prune"], #can only be these options
		dest='plottype', type=str, default='all')

	plot_parser.add_argument(
		"-c",
		"--community",
		help="Selected communities to plot. Required for plot type 'highlight', optional for plot types 'all' and 'prune'.",
		dest='community', type=str)

	plot_parser.add_argument(
		"-f",
		"--file",
		help="File name for saving plot. Can be saved as HTML, SVG, PNG, or PDF. Required.",
		dest='file', type=str, required=True)




	# metrics calculation subcommand
	metric_parser = subparser.add_parser("metric", help = "Calculate phylogenetic diversity metrics.",)

	# add long args
	metric_parser.add_argument(
		"-t",
		"--tree",
		help="Metacommunity tree. Should be Newick, NHX, or Nexus format. If given, --matrix must also be given.",
		dest='tree', type=str, default='metrics/data/mock_tree.nwk')

	metric_parser.add_argument(
		"-m",
		"--matrix",
		help="Site-by-OTU matrix of communities. Must be a CSV. If given, --tree must also be given.",
		dest='matrix', type=str, default='metrics/data/mock_matrix.csv')

	metric_parser.add_argument(
		"-d",
		"--diversity",
		help="Write diversity metrics to given CSV name. Options are Faith's PD ('fpd'), MPD ('mpd'), MNTD ('mntd'), or all three ('all'). Default is 'all'.",
		choices=["fpd", "mpd", "mntd", "all"], #can only be these options
		dest='diversity', type=str, default='all')

	metric_parser.add_argument(
		"-f",
		"--file",
		help="File name for saving plot. Should be CSV. Required.",
		dest='file', type=str, required=True)




	# simpd subcommand
	simpd_parser = subparser.add_parser("simpd", help = "Simulate communities under different phylogenetic structure assumptions.")

	#add long args
	simpd_parser.add_argument(
		"--ntips",
		help="Number of tips in the metacommunity phylogeny (number of species). Default 100.",
		dest='ntips', type=int, default=100)

	simpd_parser.add_argument(
		"--sr",
		help="Species richness of the simulated community. Required. sr must be < ntips.",
		dest='sr', type=int, required=True)

	simpd_parser.add_argument(
		"--pa",
		help="Phylogenetic assumption of the community simulation. -1: related species are least likely to co-occur; 0: no phylogenetic structure; 1: related species are most likely to co-occur. Default 0.",
		dest='pa', type=float, default = 0)

	simpd_parser.add_argument(
		"--nsites",
		help="Number of sites (rows) to simulate for the site by species matrix. Default 10.",
		dest='nsites', type=int, default = 10)

	simpd_parser.add_argument(
		"-tf",
		"--treefile",
		help="File name for saving tree data. Should be Newick. Required.",
		dest='treefile', type=str, required=True)

	simpd_parser.add_argument(
		"-cf",
		"--communityfile",
		help="File name for saving community matrix. Should be CSV. Required.",
		dest='communityfile', type=str, required=True)

	#simpd_parser.add_argument(
	#    "--df",
	#    help="Community simulation output is a numpy array when False. Output is a numpy array when True. Default False.", 
	#    dest='df', type=bool, default=True)

	#simpd_parser.add_argument(
	#    "-v", "--verbose", 
	#    help="Increase output verbosity",
	#    dest = "verbose", action="store_true")



	# parse args
	args = parser.parse_args()
	return args



# Command line script
if __name__ == "__main__":
	args = parse_command_line()

	# plotting arguments
	if args.command == "plot":
		data = Phydiv(tree = metric.tree, matrix = metric.matrix)

		if plot.plottype == 'all':
			data.plot_all(save = plot.file)
		elif plot.plottype == 'highlight':
			data.plot_highlight(community = plot.community, save = plot.file)
		elif plot.plottype == 'prune':
			data.plot_prune(save = plot.file)

		print(f"Plot(s) written to {plot.file}.")

	# metric arguments
	elif args.command == "metric":
		data = Phydiv(tree = metric.tree, matrix = metric.matrix)

		if metric.diversity == 'fpd':
			data.metric_fpd(csv = metric.file)
		elif metric.diversity == 'mpd':
			data.metric_mpd(csv = metric.file)
		elif metric.diversity == 'mntd':
			data.metric_mntd(csv = metric.file)
		elif metric.diversity == 'all':
			data.metric_all(csv = metric.file)

		print(f"Metrics written to {metric.file}.")

	# simpd arguments
	elif args.command == "simpd":
		data = Simpd(ntips = simpd.ntips)

		#write tree data
		data.sp_tree.write(path = simpd.treefile)

		#write community matrix data
		data.simmat(sr = simpd.sr, pa = simpd.pa, nsites = simpd.nsites, csv = simpd.communityfile)

		print(f"Simulated tree written to {simpd.treefile}. Simulated community written to {args.communityfile}.")















