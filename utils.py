from __future__ import division
import osmgraph


def dist(graph,path):
    path_dist = 0
    for n1, n2 in osmgraph.tools.pairwise(path):
        path_dist += graph[n1][n2]['length']
    return path_dist

def ACC(graph, shortest_path, a_star_path):
    """
    Route accuracy
    """
    return dist(graph,shortest_path) / dist(graph,a_star_path)


def RUL(graph, shortest_paths, a_star_paths):
    """
    Road usage length
    """
    shortest_dists, a_star_dists = [], []

    for path in shortest_paths:
        shortest_dists.append(dist(graph,path))
    for path in a_star_paths:
        a_star_dists.append(dist(graph,path))

    return 1 - sum(shortest_dists)/sum(a_star_dists)