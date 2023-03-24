import networkx as nx
import matplotlib.pyplot as plt

#prim
def prim(g, start):
    g = nx.Graph(g)
    bestEdges = []
    visibleEdges = []
    visibleNodes = {start}
    
    #check that there are unvisisted nodes
    while not(len(visibleNodes) == len(g.nodes())): 

        #look for all edges
        for node in visibleNodes:
            for e in list(g.edges(node, data=True)):
                visibleEdges.append(e)


        #look for minimum edge where min doesn't cycle
        do = True
        while do:
            edgeBuffer = []
            for item in visibleEdges:
                edgeBuffer.append(item[2]["weight"])

            minimumE = min(edgeBuffer) #this is the minimum weight

            #edgeBuffer is used to sort visible edges by weight

            indexofMin = edgeBuffer.index(minimumE)
            edgeWithIndex = visibleEdges[indexofMin]

            if (edgeWithIndex[1] in visibleNodes) != (edgeWithIndex[0] in visibleNodes):
                
                bestEdges.append(edgeWithIndex)
                visibleNodes.add(edgeWithIndex[1])
                visibleNodes.add(edgeWithIndex[0])
                do = False
            else:
                visibleEdges.remove(edgeWithIndex)
        
    return(bestEdges)
                
    return None

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
plt.show()

print(prim(G, 4))