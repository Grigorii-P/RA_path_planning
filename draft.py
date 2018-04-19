from __future__ import division
import osmgraph
import geog
import networkx as nx
import numpy as np
import geojsonio
import json
import itertools
from astar import A_star
from time import time
import itertools
from random import shuffle, choice
from xml_creation import nodes_xml, edges_xml

filename = '/Users/grigoriipogorelov/Desktop/map_inno.osm'
g = osmgraph.parse_file(filename)

valid_nodes = {}
for n1, n2 in g.edges():
    valid_nodes[n1] = 0
    valid_nodes[n2] = 0
    c1, c2 = osmgraph.tools.coordinates(g, (n1, n2))
    g[n1][n2]['length'] = geog.distance(c1, c2)


a_star = A_star(g, valid_nodes)

srcs = [4895039589]
dsts = [3621314698]
k_range = [1,2]
for src in srcs:
    for dst in dsts:
        a_star_path, _ = a_star.a_star_search(src,dst, k_range)

edges_xml(a_star_path)