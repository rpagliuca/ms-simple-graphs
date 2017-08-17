import networkx as nx
import matplotlib.pyplot as plt

def save(G, plot_type):
    # # Giant component
    # G = max(nx.connected_component_subgraphs(G), key=len)
    plt.clf()
    pos = nx.circular_layout(G)
    try:
        groups = nx.algorithms.bipartite.color(G)
        color_map = {0: 'green', 1: 'green'}
        colors = [color_map.get(groups.get(node)) for node in G.nodes()]
    except:
        colors = 'green'
        pass
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=1000)
    nx.draw_networkx_edges(G, pos, edge_color='grey', width=3)
    labels = {}
    for i in range(0, G.number_of_nodes()):
        labels[i] = i+1
    nx.draw_networkx_labels(G, pos, labels, font_size=14, font_color='white')
    plt.axes().set_aspect('equal', 'datalim')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("out/graph_" + plot_type + ".pdf")

# petersen = nx.petersen_graph()
# tutte = nx.tutte_graph()
# maze = nx.sedgewick_maze_graph()
# tet = nx.tetrahedral_graph()
# K_5 = nx.complete_graph(5)
# barbell = nx.barbell_graph(10,10)
# lollipop = nx.lollipop_graph(10,20)
# er = nx.erdos_renyi_graph(100,0.15)
# ws = nx.watts_strogatz_graph(30,3,0.1)
# ba = nx.barabasi_albert_graph(100,5)
# red = nx.random_lobster(100,0.9,0.9)

# Basic graph
G = nx.erdos_renyi_graph(5, 0.6)
save(G, "1_basic")

# # Complete bipartite
# G = nx.complete_bipartite_graph(3,5)

# Small-world
G = nx.watts_strogatz_graph(10,4,0.3)
save(G, "2_smallworld")

edges = [(2, 0), (2, 4), (1, 4), (2, 3), (3, 4)]
# Directed Graph
G = nx.DiGraph()
G.add_edges_from(edges)
save(G, "3_directed")

# Undirected Graph
G = nx.Graph()
G.add_edges_from(edges)
save(G, "4_undirected")

# Bipartite
G = nx.complete_bipartite_graph(3,4)
save(G, "5_bipartite")

# Custom for calculating some measures of centrality
edges = [(2, 0), (1, 2), (2, 3), (3, 4)]
# Directed Graph
G = nx.Graph()
G.add_edges_from(edges)
save(G, "6_custom")
