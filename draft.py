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
from xml_creation import *
from random import uniform



# filename = '/Users/grigoriipogorelov/Desktop/map_inno.osm'
# filename = '/Users/grigoriipogorelov/Desktop/melbourne.osm'
# g = osmgraph.parse_file(filename)
#
# valid_nodes = {}
# for n1, n2 in g.edges():
#     valid_nodes[n1] = 0
#     valid_nodes[n2] = 0
#     c1, c2 = osmgraph.tools.coordinates(g, (n1, n2))
#     g[n1][n2]['length'] = geog.distance(c1, c2)
#
#
# a_star = A_star(g, valid_nodes)
#
# # srcs = [4895039589]
# # dsts = [3621314698]
# srcs = [319710218,250286724]
# dsts = [631477263,256708681]
# paths = []
# k_range = [1,2]
# nodes_dict = {}
# for src in srcs:
#     for dst in dsts:
#         a_star_path, _ = a_star.a_star_search(src,dst, k_range)
#         paths.append(a_star_path)
#
# # single_route_vehicles_xml(a_star_path, 3, 123, 'test')
# all_xmls(g, paths, 3, 1000, 'melbourne')


import osmgraph
import geog
import geojsonio
import json
import itertools
from astar import A_star
from time import time
import itertools
from random import shuffle, choice
from utils import *

filename = '/Users/grigoriipogorelov/Desktop/melbourne.osm'
g = osmgraph.parse_file(filename)

valid_nodes = {}
for n1, n2 in g.edges():
    valid_nodes[n1] = 0
    valid_nodes[n2] = 0
    c1, c2 = osmgraph.tools.coordinates(g, (n1, n2))
    g[n1][n2]['length'] = geog.distance(c1, c2)

a_star = A_star(g, valid_nodes)










sources = [370708433]
destinations = [1928298965]
paths = []

for src, dst in itertools.izip(sources, destinations):
    path = nx.shortest_path(g, src, dst, 'length')
    coords = osmgraph.tools.coordinates(g, path)
    paths.append({'type': 'LineString', 'coordinates': coords})

k = 5
range_ = 10
k_max = k
step = (k_max-1)/range_
k_range = list(np.arange(1, k_max, step))
k_range.append(k_max)

variety = 6
a_star = A_star(g, valid_nodes)
for src, dst in itertools.izip(sources, destinations):
    for i in range(variety):
        a_star_path, _ = a_star.a_star_search(src, dst, k_range)
        coords = osmgraph.tools.coordinates(g, a_star_path)
        paths.append({'type': 'LineString', 'coordinates': coords})

geojsonio.display(json.dumps(paths))
