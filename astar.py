import heapq
import osmgraph
import geog
import networkx as nx
import itertools

#
## https://www.redblobgames.com/pathfinding/a-star/implementation.html#python-astar
#

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class A_star:
    def __init__(self, graph, valid_nodes):
        self.graph = graph
        assert type(valid_nodes) == list
        self.valid_nodes = valid_nodes

    def heuristic(self, src, dst):
        c1, c2 = osmgraph.tools.coordinates(self.graph, (src, dst))
        return geog.distance(c1, c2)

    def path_as_list(self, path_as_dict, dst):
        path_as_list = []
        path_as_list.append(dst)
        temp = dst
        while path_as_dict[temp] != None:
            path_as_list.append(path_as_dict[temp])
            temp = path_as_dict[temp]
        return path_as_list

    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in self.graph.neighbors(current):
                if next in self.valid_nodes:
                    new_cost = cost_so_far[current] + self.graph[current][next]['length']
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost + self.heuristic(goal, next)
                        frontier.put(next, priority)
                        came_from[next] = current
        return self.path_as_list(came_from, goal), cost_so_far

#
# g = nx.Graph()
# g.add_node(1, coordinate=(0,0))
# g.add_node(3, coordinate=(1,1))
# g.add_node(5, coordinate=(1,2))
# g.add_node(7, coordinate=(0,3))
# g.add_node(9, coordinate=(-2,5))
# # g.add_node(2, coordinate=(-2,1.5))
# g.add_node(2, coordinate=(0.01,2.99))
# g.add_edges_from([(1, 2), (1, 3),(2, 9),(9, 7),(3, 5),(5, 7),(2,7)])
#
# valid_nodes = []
# for n1, n2 in g.edges():
#     if n1 not in valid_nodes:
#         valid_nodes.append(n1)
#     if n2 not in valid_nodes:
#         valid_nodes.append(n2)
#     c1, c2 = osmgraph.tools.coordinates(g, (n1, n2))
#     g[n1][n2]['length'] = geog.distance(c1, c2)
#
# a_star = A_star(g, valid_nodes)
# shortest_path, _ = a_star.a_star_search(1,7)
# print(shortest_path)