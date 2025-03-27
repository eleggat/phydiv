

Questions:

1. Why require users to input sequences or IDs, instead of a phylogenetic tree? It may be easier to require them to do the work of phylogenetic inference, since there are so many possible ways to do it, and then you focus on a downstream analysis using their tree and a site-by-species matrix.

Response:

1. Goal of the project is pretty clear. But which metrics specifically do you want to implement first? MPD, NNI, etc.
2. The input data is clear, but I recommend rethinking it to simplify to trees and matrices.
3. The code looks like a good start. Because there are many possible metrics to compute you may want to write each as a separate function.

