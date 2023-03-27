import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from queue import PriorityQueue
import math

def dijkstra(g, start): #sorting attribute weight
    g=nx.Graph(g)
    predecessor = {}
    distance = {}

    pq = PriorityQueue()

    unvisited = list(g.nodes)

    for item in unvisited:
        distance[item] = math.inf
    distance[start]=0

    while len(unvisited) != 0:
        for node in distance:
            pq.put((distance[node],node))

        current = pq.get()
        cNodeName=current[1]
        cDist = current[0]
        unvisited.remove(cNodeName)

        for neighbour in g.neighbors(cNodeName):
            thisDist = distance[current[1]] + g[current[1]][neighbour]["weight"] #dict of dict model
            if thisDist < distance[neighbour]:
                distance[neighbour] = thisDist
                predecessor[neighbour] = current[1]
    

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
dijkstra(G, 4)