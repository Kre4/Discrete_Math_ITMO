import networkx as nx
import matplotlib.pyplot as plt
from help_functions import *
from networkx.algorithms import approximation, connectivity

null_degree_nodes = ["CY", "IS", "MT"]
COLORS = ["b", "g", "y", "#9457EB", "#004242", "#FF43A4", "#FA8837", "#05AFB2", "#B22030", "#A0785A"]


def solve_b(G):
    Graph = nx.Graph(G)
    print("|V| = " + str(len(Graph.nodes)))
    print("|E| = " + str(len(Graph.edges)))
    max_degree = -1
    min_degree = 1000
    for ISO in Graph.nodes:
        if Graph.degree[ISO] > max_degree:
            max_degree = Graph.degree[ISO]
        if Graph.degree[ISO] < min_degree:
            min_degree = Graph.degree[ISO]
    print("Min deg = " + str(min_degree))
    print("Max deg = " + str(max_degree))
    Graph = biggest_component(Graph)
    print("Radius = " + str(nx.radius(Graph)))
    print("Diameter = " + str(nx.diameter(Graph)))
    print("Girth = " + str(len(nx.minimum_cycle_basis(G)[0])) + ". Example: " + str(nx.minimum_cycle_basis(G)[0]))
    print("Center: " + str(nx.center(Graph)))

    print("Edge connectivity = " + str(nx.edge_connectivity(Graph)))
    print("Node connectivity = " + str(nx.node_connectivity(Graph)))


def solve_c(G):
    # Clique 4 [MK, GR, TR, BG]
    f = open("txt_sources/vertex_coloring")
    colors = dict()
    nodes = (G.nodes.keys())
    for line in f.readlines():
        colors[line.split(',')[0]] = int(line.split(', ')[1])

    nodes_color = list()

    for i in nodes:
        nodes_color.append(colors[i])

    print("Vertex coloring size = " + str(len(set(nodes_color))))
    show_graph(G, color=nodes_color, name="png/vertex_coloring.png")


def solve_d(G):
    Graph = biggest_component(G)

    f = open("txt_sources/edge_coloring")
    colors = list()
    for line in f.readlines():
        colors.append(COLORS[int(line.split(" ")[2])])
    show_graph(Graph, edge_color=colors)


def solve_e(G):
    clique = (nx.enumerate_all_cliques(G))
    for item in clique:
        print(item)


def solve_f(G):
    Graph = biggest_component(G)
    in_set = nx.algorithms.approximation.clique.clique_removal(Graph)
    print("Size of independent set: " + str(len(in_set[0])))
    for item in in_set[0]:
        print(item)


def solve_g(G):
    Graph = biggest_component(G)
    max_w = nx.max_weight_matching(Graph, maxcardinality=True, weight=0)

    for item in max_w:
        print(item)
    print(len(max_w))


def solve_h(G):
    Graph = biggest_component(G)
    cover = nx.algorithms.approximation.min_weighted_vertex_cover(Graph)
    for item in cover:
        print(item)
    print(len(cover))


def solve_i(G):
    Graph = biggest_component(G)
    cover = nx.algorithms.min_edge_cover(Graph)
    for item in cover:
        print(item)
    print(len(cover))


def solve_j(G):
    # ['HR', 'SL', 'IT', 'CH', 'DE', 'CZ', 'SK', 'UA', 'RO', 'RS']
    Graph = biggest_component(G)
    f = open("txt_sources/task_j")
    colors = list()
    for line in f.readlines():
        colors.append(COLORS[int(line.split(" ")[2])])
    show_graph_for_j(Graph, edge_color=colors)


def solve_k(G):
    Graph = biggest_component(G)
    make_color_edge_file()
    show_graph(Graph)


def solve_l(G):
    comp = nx.k_components(G)[2]
    nodes = dict()
    for i in G.nodes:
        nodes[i] = "#FFFFFF"
    i = 1
    for component in comp:
        for ISO in component:
            nodes[ISO] = COLORS[i]
        i += 1
    color = list()
    for c in nodes:
        color.append(nodes[c])
    block_cut_tree = nx.Graph()
    block_cut_tree.add_nodes_from([1, 2, 3])
    block_cut_tree.add_edges_from([(1, 2), (3, 2)])
    show_graph(G, color=color)
    show_graph(block_cut_tree, color=[COLORS[1], COLORS[3], COLORS[2]])


def solve_l_2nd_variant(G):
    adjacency_list(G)
    parse_adjacency_list_for_sage()


def solve_m(G):
    components = nx.algorithms.connectivity.edge_kcomponents.bridge_components(G)
    components = sorted(map(sorted, components))
    nodes = dict()
    for node in G.nodes:
        nodes[node] = 0
    i = 1
    for comp in components:
        for ISO in comp:
            nodes[ISO] = i
        i += 1
    colors = list()
    for item in nodes:
        colors.append(nodes[item])
    show_graph(G, color=colors, needToSave=False, name="png/task_m")


def solve_n(G):
    biconnected_component = max((list(nx.biconnected_components(biggest_component(G)))), key=len)
    Graph = nx.Graph()
    f = open("test.txt")
    for line in f.readlines():
        tmp = line.split(", ")
        if tmp[0] in biconnected_component:
            if tmp[1] in biconnected_component:
                Graph.add_edge(tmp[0], tmp[1])
    f.close()
    adjacency_list(Graph)
    parse_adjacency_list_for_sage()
    # run sage script
    show_graph(Graph)


def solve_o(G, show_the_tree=False):
    Graph = biggest_component(G)
    mst = nx.Graph(nx.minimum_spanning_tree(Graph))
    weight = 0
    for node in mst.adj:
        for edge in mst.adj[node]:
            weight += (mst.adj[node][edge]["weight"])
    print(weight / 2)

    # 13939

    if show_the_tree:
        show_tree(mst, show_weight=True)
    return mst


def solve_p(G):
    mst = solve_o(G, show_the_tree=False)
    min = 100000000000
    centroid = []
    for node in mst.nodes:
        current_weight = max(dfs_weight(mst, node))
        if current_weight < min:
            min = current_weight
            centroid = []
            print(min)
        if current_weight == min:
            centroid.append(node)
    print(dfs_weight(mst, 'AL'))
    print(str(centroid) + str(min))
    show_tree(mst)


def solve_q(G):
    mst = solve_o(G, show_the_tree=False)
    new_mst = nx.Graph()
    new_nodes = dict()

    i = 0
    for node in mst.nodes:
        new_nodes[node] = i
        i += 1
    for edge in mst.edges:
        new_mst.add_edge(new_nodes[edge[0]], new_nodes[edge[1]])
    prufer = nx.to_prufer_sequence(new_mst)
    correct_prufer = list()
    for number in prufer:
        correct_prufer.append(list(new_nodes.keys())[list(new_nodes.values()).index(number)])

    print(correct_prufer)
