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
import xml.etree.ElementTree
from utils import *

filename = '/Users/grigoriipogorelov/Desktop/melbourne.osm'
# filename = '/Users/grigoriipogorelov/Desktop/inno.osm'
g = osmgraph.parse_file(filename)

valid_nodes = {}
for n1, n2 in g.edges():
    valid_nodes[n1] = 0
    valid_nodes[n2] = 0
    c1, c2 = osmgraph.tools.coordinates(g, (n1, n2))
    g[n1][n2]['length'] = geog.distance(c1, c2)

a_star = A_star(g, valid_nodes)



num_cars = [50,100,200,500,1000,1500,2000]
num_cars_back = 5000
type_cars_variety = 20

sources = [370708433]
destinations = [1928298965]

shortest_paths, a_paths = [], []
for src, dst in itertools.izip(sources, destinations):
    path = nx.shortest_path(g, src, dst, 'length')
    shortest_paths.append(path)

k = 2
range_ = 10
k_max = k
step = (k_max - 1) / range_
k_range = list(np.arange(1, k_max, step))
k_range.append(k_max)

variety = 20
a_star = A_star(g, valid_nodes)
for src, dst in itertools.izip(sources, destinations):
    for i in range(variety):
        a_star_path, _ = a_star.a_star_search(src, dst, k_range)
        a_paths.append(a_star_path)

for n_cars in num_cars:
    all_xmls(g, shortest_paths, type_cars_variety, n_cars, num_cars_back, True, 'maps/melbourne_sh/melbourne_sh_' + str(n_cars))
    all_xmls(g, a_paths, type_cars_variety, n_cars, num_cars_back, False, 'maps/melbourne_a/melbourne_a_' + str(n_cars))