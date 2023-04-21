import networkx as nx
import matplotlib.pyplot as plt



def DFSr(g, s, visited):
    visited.append(s)
    g = nx.DiGraph(g)
    for neighbour in g.neighbors(s):
        if neighbour not in visited:
            visited = DFSr(g,neighbour,visited)
    return visited


def DFSr2(g,s,visited,t,x,tn): #tn is a list of nodes which have treasure.
    if s in tn:
        t = t+1
        if t >= x:
            return visited
    if s not in visited:
        visited.append(s)
    g = nx.DiGraph(g)
    for neighbour in g.neighbors(s):
        if neighbour not in visited:
            if visited == DFSr2(g,neighbour,visited,t,x,tn):
                return []
            else:
                return DFSr2(g,neighbour,visited,t,x,tn)

    return visited



a=nx.DiGraph()
a.add_edges_from([('S','d'),('d','b'), ('b','a'),('b','c')])
a.add_edges_from([('S','e'),('e','f'),('e','g'),('f','h'),('h','j'),('j','i')])
pos = nx.planar_layout(a)
# nodes
nx.draw_networkx_nodes(a, pos, node_size=700, node_color='lightgrey')
nx.draw_networkx_labels(a,pos,font_color = 'blue')
# edges     
nx.draw_networkx_edges(a, pos, width=4, edge_color ='red')
print(DFSr2(a,"S",[],0,3,["e","b","c"]))
plt.axis("off")
plt.show()
