# igraph-python
Clean examples of `igraph` code for building graphs with nodes and edges.  

`igraph` is a package written in C that allows the creation, management and plotting of graphs. It works by handling state, rather than by passing messages (like Akka or Orleans). `igraph` was used to generate the synthetic retail data used as a running example through various of my repos.

- 12 stores  
- 3970 products  
- 63 days (9 weeks)

### packages used
 
`igraph`: create graphs, manage state and also to create plots.  
`matplotlib.pyplot`: used in this repo to render `igraph` plots.

### data/
synthetic_data.npz. Compressed Numpy file containing three arrays:

dates: (63, ) array of integers (not dates).  
synth_sales_data: (12, 3970, 63) array of integer sales quantities.  
fitted_line: (12, 3970, 63) array of doubles fitted through the sales quantities.  
synthetic_data.csv.gz. Compressed csv file containing the same data as the .npz file but in long format.  

### src/

`graphlayout.py`: the entry point of the code.  
`graph.py`: uses `igraph` to create a graph.  
`visualisation.py`: plots the graph structure.  
