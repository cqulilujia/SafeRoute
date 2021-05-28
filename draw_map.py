import matplotlib.pyplot as plt
import pickle
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib.pyplot import MultipleLocator

f = open('./data/nxGraph_boston.gpickle', 'rb')
G_boston_1 = G_boston = pickle.load(f, encoding='iso-8859-1')
# G_boston = G_boston_1.to_undirected()

coord_boston = pd.read_csv('./data/entity2id_boston.txt', header=None, delimiter='\s|,', engine='python')
pos_boston = coord_boston[[1, 0]].to_numpy()
id_boston = coord_boston[2].to_numpy()
npos_boston = dict(zip(id_boston, pos_boston))

order_int = np.linspace(0, id_boston.size, num=id_boston.size).astype(int)
nlabels_boston = dict(zip(id_boston, order_int))  # 标志字典，构建节点与标识点之间的关系

print('number of nodes', G_boston.number_of_nodes())
print('number of edges', G_boston.number_of_edges())

fig = plt.figure()
ax = fig.add_subplot()

x_max, y_max = pos_boston.max(axis=0)  # 获取每一列最大值
x_min, y_min = pos_boston.min(axis=0)  # 获取每一列最小值
x_num = (x_max - x_min) / 30
y_num = (y_max - y_min) / 30
print(x_max, y_max, x_min, y_min)

ax.set(xlim=[x_min-x_num, x_max+x_num], ylim=[y_min-y_num, y_max+y_num], title='Map',
       ylabel='Y-Axis', xlabel='X-Axis')

nx.draw_networkx_nodes(G_boston, npos_boston, node_size=20, node_color="#6CB6FF", ax=ax, label=True)  # 绘制节点
nx.draw_networkx_edges(G_boston, npos_boston, G_boston.edges(), ax=ax, arrows=False, arrowstyle='-|>', arrowsize=7, edge_color="k")  # 绘制边
# nx.draw_networkx_labels(G_boston,npos_boston, nlabels_boston, font_size=7, font_color="r")
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)

# nx.draw(G_boston, node_size=50)
plt.show()
