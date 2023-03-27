from queue import PriorityQueue as pq
import networkx as nx
import matplotlib.pyplot as plt


def bestFirstSearch(g, start, end):
    g = nx.Graph(g)
    print(nx.to_dict_of_dicts(g))
    toVisit = pq()
    toVisit.put((0,start))
    visited = []
    predecessor = {}

    while not toVisit.empty():
        current = toVisit.get()[1]
        visited.append(current)

        for neighbour in g[current]:
            if neighbour not in visited:
                predecessor[neighbour]=current
                nodeweight = g.nodes[neighbour]["weight"] #heuristic here
                toVisit.put((nodeweight,neighbour))
                if neighbour==end:
                    print("found")
                    return predecessor, visited

graphData = {
    "a":{"b":{}, "c":{}},
    "b":{"a":{},"d":{},"f":{},"e":{}},
    "c":{"a":{},"g":{}},
    "d":{"b":{}},
    "e":{"b":{},"h":{}},
    "f":{"b":{}},
    "g":{"c":{},"i":{}},
    "h":{"e":{},"i":{}},
    "i":{"j":{},"h":{},"g":{}},
    "j":{"i":{}}
}



nodeData = {
    "a":{"weight":4},
    "b":{"weight":2},
    "c":{"weight":3},
    "d":{"weight":3},
    "e":{"weight":2},
    "f":{"weight":1},
    "g":{"weight":2},
    "h":{"weight":2},
    "i":{"weight":1},
    "j":{"weight":0}
}

g = nx.Graph()
g = nx.from_dict_of_dicts(graphData) #technically not necessary, but somewhat more readable w/ 2


for key in nodeData:
    for key2 in nodeData[key]:
        g.nodes[key][key2]=nodeData[key][key2]

#draw nodes (input each node as its own list separately, get data from nodeData dict)
pos = nx.spring_layout(g)
for node in nodeData:
    nx.draw_networkx_nodes(g,pos, nodelist=[node], node_color="white", edgecolors=nodeData[node].get("colour","black")) # nodelist[node] means just the 1 node
  
#create a dict just for getting edge labels
edge_labels ={} 
  
#note to self that each item in g.edges is a 2-tuple or 3-tuple depending on data=true or false
#a la (0:node1, 1:node2, 2:dict)
for item in g.edges(data=True):
    nx.draw_networkx_edges(g,pos,edgelist=[item],edge_color=item[2].get("colour","black"), width=item[2].get("thickness",1))
    edge_labels[(item[0],item[1])]=item[2].get("label","") #add item to edge label
  
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(g,pos)
print(bestFirstSearch(g,"b","i"))
#plt.show()