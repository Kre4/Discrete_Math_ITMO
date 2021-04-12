import networkx as nx
import matplotlib.pyplot as plt


null_degree_nodes = ["CY", "IS", "MT"]
COLORS = ["b", "g", "y", "#9457EB", "#004242", "#FF43A4", "#FA8837", "#05AFB2", "#B22030", "#A0785A"]


def biggest_component(G):
    Graph = nx.Graph(G)
    Graph.remove_nodes_from(null_degree_nodes)
    component = min(nx.connected_components(Graph), key=len)
    Graph.remove_nodes_from(component)
    if not nx.is_connected(Graph):
        raise Exception("smt wrong")
    return Graph


def show_tree(G, show_weight=False):
    nx.draw(G, pos=nx.kamada_kawai_layout(G), with_labels=True)

    if show_weight:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=nx.kamada_kawai_layout(G), edge_labels=labels, font_size=6)

    plt.show()


def dfs(Graph, v, starter, visited, result, i):
    if v == starter and visited[v] == True:
        return
    visited[v] = True

    for node in Graph.neighbors(v):
        if not visited[node]:
            result[i] += Graph.get_edge_data(v, node)['weight']
            dfs(Graph, node, starter, visited, result, i)


def dfs_weight(G, vertex):
    Graph = nx.Graph(G)
    visited = dict()
    for node in Graph.nodes:
        visited[node] = False
    rrr = Graph.neighbors(vertex)
    result = [0] * 4
    i = 0
    for r in Graph.neighbors(vertex):
        for k in Graph.neighbors(vertex):
            visited[k] = True
        visited[vertex] = False
        visited[r] = False
        dfs(Graph, vertex, vertex, visited, result, i)
        i += 1
    for i in range(0, len(result)):
        if result[i] == 0:
            result[i] = -999999

    return result
    # 4685


def show_graph(G, color='r', edge_color='b', name="picture.png", needToSave=False, show_weight=False):
    plt.subplot(111)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos=nx.planar_layout(G), node_color=color, edge_color=edge_color, with_labels=True)
    if show_weight:
        nx.draw_networkx_edge_labels(G, pos=nx.planar_layout(G), edge_labels=labels, font_size=6)
    if not needToSave:
        plt.show()
    else:
        plt.savefig(name, dpi=1000)


def show_graph_for_j(G, color='r', edge_color='b', name="picture.png", needToSave=False):
    plt.subplot(111)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos=nx.planar_layout(G), node_color=color, edge_color=edge_color, with_labels=True, node_size=0,
            font_size=13)
    # nx.draw_networkx_edge_labels(G, pos=nx.planar_layout(G), edge_labels=labels, font_size=6)
    if not needToSave:
        plt.show()
    else:
        plt.savefig(name, dpi=1000)


def make_color_file(G):
    coloring = nx.greedy_color(G, strategy="DSATUR")
    f = open("vertex_coloring", "w")
    for item in coloring:
        f.write(item + ", " + str(coloring[item]) + "\n")


def make_color_edge_file(G, filename="edge_coloring"):
    Graph = biggest_component(G)
    f = open(filename, "w")
    edges = Graph.edges
    for item in edges:
        f.write(item[0] + " " + item[1] + " 0\n")
    f.close()


def adjacency_list(G):
    nx.write_adjlist(G, "txt_sources/adjacency_list")


def was_it_taken_j(G):
    f = open("txt_sources/task_j")
    unique = set()
    for line in f.readlines():
        unique.add(line.split(" ")[0])
        unique.add(line.split(" ")[1])
    print("The same amount?")
    print(len(biggest_component(G).edges) == len(unique))


def parse_adjacency_list_for_sage():
    f = open("txt_sources/adjacency_list")

    result = "{"
    i = 0
    for line in f.readlines():
        if i < 3:
            i += 1
        else:
            tmp = line.split(" ")
            first = True
            if len(tmp) != 1:
                for item in tmp:
                    if first:
                        result += "\"" + item + "\":["
                        first = False
                    else:
                        if len(item) == 3:
                            item = item[:2]
                        result += "\"" + item + "\""
                        if item == tmp[len(tmp) - 1][:2]:
                            result += "],"
                        else:
                            result += ","

    print(result[:len(result) - 1] + "}")
