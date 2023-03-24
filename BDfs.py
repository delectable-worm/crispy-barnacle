import networkx as nx
import matplotlib.pyplot as plt
import queue
from collections import deque

def BFS(g, start):

    g = nx.Graph(g)
    nextNodes = queue.Queue(0)
    nodesVisited = []
    nextNodes.put(start)
    while not nextNodes.empty():

        current = nextNodes.get()

        queue2list = list(nextNodes.queue)

        for node in g.neighbors(current):
            if node not in nodesVisited and node not in queue2list:
                nextNodes.put(node)
        
        nodesVisited.append(current)


    return nodesVisited


def BFSlayers(g, start):

    g = nx.Graph(g)
    nextNodes =deque()
    nextNodes.append(start)

    nextNodesLayers=deque()
    nextNodesLayers.append(0)

    visitedNodes = []
    visitedNodesLayers =[]
    
    while not len(nextNodes) == 0:
        current = nextNodes.popleft()
        visitedNodes.append(current)

        currentLayer = nextNodesLayers.popleft()
        visitedNodesLayers.append(currentLayer)

        for neighbour in g.neighbors(current):
            if neighbour not in nextNodes and neighbour not in visitedNodes:
                nextNodes.append(neighbour)
                nextNodesLayers.append(currentLayer+1)

        
    print(visitedNodesLayers)
    print(visitedNodes)
    return None



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

print(nx.get_edge_attributes(G,"weight"))

#BFSlayers(G, 4)
#plt.show()