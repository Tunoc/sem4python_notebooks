### [Wikipedia data](https://snap.stanford.edu/data/wiki-Vote.html)  
Use python to download the `.txt.gz` file.  

# Exercise1:  
1)	Create a python notebook, and download the dataset from the link above.  
2)	Use python to create a new file and copy all the data from the `.txt.gz` into a `.txt` file.  
3)  Use `networkx` to add the nodes from the file we just created: [NetworkX_Documentation](https://networkx.org/documentation/stable/reference/classes/graph.html)  
4)  Make a random number generator that is able to create a number between 1 and the length of your Undirected graphs.  
5)  Print all the neighbouring nodes, of the randomly generated id.  
6)  Make a visual presentation of the randomly generated id in the notebooks. `nx.draw()`

# Exercise2:
1)  Make a simple flask server with one, get endpoint `/wiki/randomNodes`.  
    a) Make it write `Hello World`.  
2)	Edit the `/wiki/randomNodes` endpoint to print the randomly generated node, and all the neightboring nodes.  

### Made by:  
## *Lucky drawing*  
