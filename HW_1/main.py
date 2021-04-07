import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation, connectivity
from solvers import *
import re



f = open("txt_sources/test.txt")
G = nx.Graph()
lines = f.readlines()
edges = list()
for line in lines:
    tmp = re.split(', | -', line)
    tmp[2] = int(tmp[2])

    edges.append(tmp)

G.add_weighted_edges_from(edges)
# G.add_edges_from(edges)

G.add_nodes_from(null_degree_nodes)
# solve_b(G)
# solve_c(G)
# solve_d(G)
# solve_e(G)
# solve_f(G)
# solve_g(G)
# solve_h(G)
# solve_i(G)
# make_color_edge_file(G=G, filename="task_j")
# was_it_taken_j(G)
# solve_j(G)
# solve_k(G)
# solve_l_2nd_variant(G)
# solve_m(G)
# solve_n(G)
# solve_o(G,show_the_tree=True)
# solve_p(G)

solve_q(G)
