setwd("/Users/emilyleggat/Documents/GitHub/hacks/phydiv/notebooks")

library(tidyverse)
library(picante)

#load in data and convert dm to matrix
comm_data <- read_csv("testing2.csv")
tree_data <- read.tree("testing2_tree.nwk")
dm_data_raw <- read_csv("testing2_dm.csv")
dm_data_raw <- as.matrix(dm_data_raw)

dm_data <- dm_data_raw[,-1]
rownames(dm_data) <- dm_data_raw[,1]

# For each community, calculate different diversity measures

#faith's
pd <- pd(comm_data, tree_data, include.root = TRUE)

#mpd
mpd <- mpd(comm_data, dm_data)

#mnnd

