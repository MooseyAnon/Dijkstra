## Dijkstra's algorithm for a particular input format 
----------------------------------------------------------------
*(first draft)

run.py takes the commandline arguments- the graph, start node, end node 

```bash 

./run.py graph start end

```

# Input format

the input must have the format:


 

nodeID 
  . 
  .
  .
nodeID

nodeID nodeID distance/weight 
  .
  .
  .
nodeID nodeID distance/weight

i.e. a list of nodes followed by list of edges with weights


Currently designed to work with integers but can easily be modified. 
