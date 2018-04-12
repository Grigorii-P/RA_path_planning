import osmgraph
import geog
import networkx as nx
import geojsonio
import json
import itertools


filename = '/Users/grigoriipogorelov/Downloads/map_inno.osm'
g = osmgraph.parse_file(filename)

for n1, n2 in g.edges():
    c1, c2 = osmgraph.tools.coordinates(g, (n1, n2))   
    g[n1][n2]['length'] = geog.distance(c1, c2)
    
start = 3598458167
# end = 4380221998
end = 4895039587
path = nx.shortest_path(g, start, end, 'length')
coords = osmgraph.tools.coordinates(g, path)

geojsonio.display(json.dumps({'type': 'LineString', 'coordinates': coords}))


dist = 0
for n1, n2 in osmgraph.tools.pairwise(path):
    dist += g[n1][n2]['length']
print(dist)
