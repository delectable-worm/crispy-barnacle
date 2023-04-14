import networkx as nx
import matplotlib.pyplot as plt
import math
#prim


def prim2(g):
    minWeight = math.inf
    g = nx.Graph(g)
    cost = 0
    edges = []
    mstNodes = [list(g)[0]]
    print(mstNodes)
    print(list(g))
    while len(mstNodes) != len(list(g)):
        for u in mstNodes:
            for v in g.neighbors(u):
                if not v in mstNodes:
                    if minWeight > g[u][v]["weight"]:
                        minWeight = g[u][v]["weight"]
                        x = u
                        y = v
        mstNodes.append(y)
        print(mstNodes)
        edges.append((x,y,minWeight))
        cost += minWeight
        minWeight = math.inf
    return cost
            

    

# Python3/Trinket 3.6 Breakout Activity Graph 
import matplotlib.pyplot as plt 
import networkx as nx 
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


print(prim2(G))