import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
import math

def bf(g, start): #nicer, neater
    predecessor = {}
    distance = {}
    getWeight = nx.get_edge_attributes(g,"weight")
    g = nx.DiGraph(g)

    for node in g.nodes():
        distance[node] = math.inf
    distance[start]=0

    for i in range(g.number_of_nodes()-1):
        for (u,v,d) in g.edges.data("weight"):
            if distance[u] + d < distance[v]:
                distance[v]=distance[u]+d
                predecessor[v]=u

    for (u,v,d) in g.edges.data("weight"):
            if distance[u] + d < distance[v]:
                return 1
    
    return predecessor,distance


G=nx.Graph() 
# weighted edges for 3.6 activity 
G.add_edge(4,5,weight=3.5) 
G.add_edge(4,7,weight=3.7) 
G.add_edge(5,7,weight=2.8) 
G.add_edge(0,7,weight=1.6) 
G.add_edge(1,5,weight=3.2) 
G.add_edge(0,4,weight=3.8) 
G.add_edge(2,3,weight=1.7) 
G.add_edge(1,7,weight=1.9) 
G.add_edge(0,2,weight=2.6) 
G.add_edge(1,2,weight=3.6) 
G.add_edge(1,3,weight=2.9) 
G.add_edge(2,7,weight=3.4) 
G.add_edge(6,2,weight=4.0) 
G.add_edge(3,6,weight=5.2) 
G.add_edge(4,5,weight=3.5) 
G.add_edge(6,0,weight=5.8) 
G.add_edge(6,4,weight=9.3) 
 
pos = nx.shell_layout(G) # position nodes on canvas 
nx.draw_networkx_nodes(G, pos, node_size=1000,node_color='LightGray') 
nx.draw_networkx_labels(G, pos, font_size=20,font_family='sans-serif') 
nx.draw_networkx_edges(G, pos, width=3, edge_color='LightBlue') 
 
edge_labels=dict([((u,v),d['weight']) 
for u,v,d in G.edges(data=True)]) 
nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels) 
 
plt.axis('off')
print(bf(G, 4))