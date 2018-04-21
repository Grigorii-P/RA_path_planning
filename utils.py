from __future__ import division
import osmgraph


def dist(graph,path):
    path_dist = 0
    for n1, n2 in osmgraph.tools.pairwise(path):
        try:
            path_dist += graph[n1][n2]['length']
        except KeyError:
            path_dist += graph[n2][n1]['length']
    return int(path_dist)

def ACC(shortest, a_star):
    """
    Route accuracy
    """
    return shortest / a_star


def RUI(shortests, a_stars):
    """
    Road usage length
    """

    return 1 - sum(shortests)/sum(a_stars)