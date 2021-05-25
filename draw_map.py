import matplotlib.pyplot as plt
import pickle
import networkx as nx

G = nx.read_gpickle("./data/nxGraph_boston.gpickle")
print(type(G))

nx.draw(G)
plt.show()

print('number of nodes', G.number_of_nodes())
print('number of edges', G.number_of_edges())