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

folder_sh = '/Users/grigoriipogorelov/Desktop/RA_project/RA_rand_path_planning/maps/melbourne_sh/results_sh_'
folder_a = '/Users/grigoriipogorelov/Desktop/RA_project/RA_rand_path_planning/maps/melbourne_a/results_a_'
num_vehicles = ['50','100','200','500','1000','1500','2000']
shortest_paths = []
a_paths = []
for n in num_vehicles:
    path_sh = folder_sh + n + '.xml'
    path_a = folder_a + n + '.xml'
    mean_short = mean_time(path_sh)
    mean_a = mean_time(path_a)
    shortest_paths.append(mean_short)
    a_paths.append(mean_a)

print