from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.ElementTree as ET
import xml.dom.minidom
from random import uniform, randint


def nodes_xml(graph, paths, file_name):
    nodes_dict = {}
    if type(paths[0]) == int:
        for node in paths:
            nodes_dict[node] = 0
    else:
        for path in paths:
            for node in path:
                nodes_dict[node] = 0


    nodes = Element('nodes')
    for node in nodes_dict:
        id = str(node)
        coords = graph.node[node]['coordinate']
        x = str(coords[0])
        y = str(coords[1])
        node = SubElement(nodes, 'node', {'id': id, 'x': x, 'y': y})
    tree = ET.ElementTree(nodes)
    tree.write(file_name + ".nod.xml")

def multiple_edges_xml(paths, file_name):
    edges = Element('edges')

    for path in paths:
        first = path[0]
        for i in range(1, len(path)):
            from_ = str(first)
            to_ = str(path[i])
            id = from_ + '_' + to_
            first = path[i]
            edge = SubElement(edges, 'edge', {'from': from_, 'id': id, 'to': to_})

    tree = ET.ElementTree(edges)
    tree.write(file_name + ".edg.xml")

    xml_ = xml.dom.minidom.parseString(tostring(edges))
    # print xml_.toprettyxml()

def multiple_route_vehicles_xml(paths, num_vehicle_types, num_cars, num_back_cars, is_shortest_path, file_name):
    num_cars_in_flow = int(num_cars/len(paths))
    num_cars_in_back_flow = int(num_back_cars / len(paths))
    routes = Element('routes')

    for i in range(num_vehicle_types):
        accel = str(round(uniform(0.5, 5.0), 1))
        decel = str(round(uniform(2.0, 8.0), 1))
        id = 'Car'+str(i)
        length = str(round(uniform(5, 25), 1))
        maxSpeed = str(randint(60, 120))
        sigma = str(uniform(0.0, 1.0))
        vType = SubElement(
            routes, 'vType', {'accel':accel, 'decel':decel, 'id':id, 'length':length, 'maxSpeed':maxSpeed, 'sigma':sigma})
    vType = SubElement(
        routes, 'vType',
        {'accel': accel, 'decel': decel, 'id': 'back_car', 'length': length, 'maxSpeed': maxSpeed, 'sigma': sigma})

    for i, path in enumerate(paths):
        first = path[0]
        full_route = ''
        for j in range(1, len(path)):
            from_ = str(first)
            to_ = str(path[j])
            id = from_ + '_' + to_
            full_route += id + ' '
            first = path[j]
        route = SubElement(routes, 'route', {'id':'route'+str(i), 'edges':full_route})


    for i in range(len(paths)):
        begin = "0"
        departPos = "0"
        id = str(i)
        period = "1"
        number = str(num_cars_in_flow)
        num_back = str(num_cars_in_back_flow)
        route = 'route'+str(i)
        if is_shortest_path:
            num_flows_for_shortest_path = 20
            number = str(int(num_cars_in_flow/num_flows_for_shortest_path))
            for n in range(num_flows_for_shortest_path):
                id = str(n)
                type = "Car" + str(randint(0, num_vehicle_types-1))
                flow = SubElement(
                    routes, 'flow',
                    {'begin':begin, 'departPos':departPos, 'id':id,
                     'period':period, 'number':number, 'route':route, 'type':type})
            flow = SubElement(
                routes, 'flow',
                {'begin': begin, 'departPos': departPos, 'id': 'back_flow',
                 'period': period, 'number': str(num_back_cars), 'route': route, 'type': 'back_car'})
        else:
            type = "Car" + str(randint(0, num_vehicle_types-1))
            flow = SubElement(
                routes, 'flow',
                {'begin': begin, 'departPos': departPos, 'id': id,
                 'period': period, 'number': number, 'route': route, 'type': type})
            id_back = str(i)
            flow = SubElement(
                routes, 'flow',
                {'begin': begin, 'departPos': departPos, 'id': 'back_flow'+id_back,
                 'period': period, 'number': num_back, 'route': route, 'type': 'back_car'})




    tree = ET.ElementTree(routes)
    tree.write(file_name + ".rou.xml")

def all_xmls(graph, paths, num_vehicle_types, num_cars, num_cars_in_back, is_shortest_path, file_name):
    nodes_xml(graph, paths, file_name)
    multiple_edges_xml(paths, file_name)
    multiple_route_vehicles_xml(paths, num_vehicle_types, num_cars, num_cars_in_back, is_shortest_path, file_name)





























