import networkx as nx
import matplotlib.pyplot as plt

graphData = {
    "a":{"b":{"weight":2},"e":{"weight":3}},
    "b":{"f":{"weight":1},"c":{"weight":7, "colour":"red", "thickness":5}},
    "c":{"f":{"weight":4},"d":{"weight":9}},
    "d":{"f":{"weight":4},"e":{"weight":8, "colour":"blue", "thickness":5}},
}

nodeData = {
    "a":{"colour":"black"},
    "b":{"colour":"red"},
    "c":{"colour":"red"},
    "d":{"colour":"blue"},
    "e":{"colour":"blue"},
    "f":{"colour":"black"},
}
g2 = nx.Graph()
g2 = nx.from_dict_of_dicts(graphData)

pos = nx.spring_layout(g2)
for node in nodeData:
    nx.draw_networkx_nodes(g2,pos, nodelist=[node], node_color="white", edgecolors=nodeData[node]["colour"])

edge_labels ={} 

for item in g2.edges(data=True):
    nx.draw_networkx_edges(g2,pos,edgelist=[item],edge_color=item[2].get("colour","black"), width=item[2].get("thickness",1))
    edge_labels[(item[0],item[1])]=item[2]["weight"]

nx.draw_networkx_edge_labels(g2, pos, edge_labels=edge_labels)

nx.draw_networkx_labels(g2,pos)
plt.show()
print(g2)
print(g2.edges())