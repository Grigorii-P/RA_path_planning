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
        #TODO instead of int key, make it str?
        id = str(node)
        coords = graph.node[node]['coordinate']
        x = str(coords[0])
        y = str(coords[1])
        node = SubElement(nodes, 'node', {'id': id, 'x': x, 'y': y})
    tree = ET.ElementTree(nodes)
    tree.write(file_name + ".nod.xml")

    xml_ = xml.dom.minidom.parseString(tostring(nodes))
    # print xml_.toprettyxml()

def single_edges_xml(path, file_name):
    edges = Element('edges')
    first = path[0]
    for i in range(1, len(path)):
        from_ = str(first)
        to_ = str(path[i])
        id = from_+'_'+to_
        first = path[i]
        edge = SubElement(edges, 'edge', {'from': from_, 'id': id, 'to': to_})
    tree = ET.ElementTree(edges)
    tree.write(file_name + ".edg.xml")

    xml_ = xml.dom.minidom.parseString(tostring(edges))
    # print xml_.toprettyxml()

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

def single_route_vehicles_xml(path, num_vehicle_types, num_cars, file_name):
    num_cars_in_flow = num_cars
    routes = Element('routes')

    for i in range(num_vehicle_types):
        accel = str(round(uniform(0.5, 3.0), 1))
        decel = str(round(uniform(4.0, 6.0), 1))
        id = 'Car'+str(i)
        length = str(round(uniform(10, 25), 1))
        maxSpeed = str(randint(60, 120))
        sigma = '0.0'
        vType = SubElement(
            routes, 'vType', {'accel':accel, 'decel':decel, 'id':id, 'length':length, 'maxSpeed':maxSpeed, 'sigma':sigma})

    first = path[0]
    full_route = ''
    for i in range(1, len(path)):
        from_ = str(first)
        to_ = str(path[i])
        id = from_ + '_' + to_
        full_route += id + ' '
        first = path[i]
    route = SubElement(routes, 'route', {'id':'route0', 'edges':full_route[:-1]})
    tree = ET.ElementTree(routes)
    tree.write(file_name + ".rou.xml")


    begin = "0"
    departPos = "0"
    id = '0'
    period = "1"
    number = str(num_cars_in_flow)
    route = 'route0'
    type = "Car"+str(randint(0,num_vehicle_types))
    flow = SubElement(
        routes, 'flow',
        {'begin':begin, 'departPos':departPos, 'id':id, 'period':period, 'number':number, 'route':route, 'type':type})

    xml_ = xml.dom.minidom.parseString(tostring(routes))
    print(xml_.toprettyxml())

def multiple_route_vehicles_xml(paths, num_vehicle_types, num_cars, file_name):
    num_cars_in_flow = int(num_cars/len(paths))
    routes = Element('routes')

    for i in range(num_vehicle_types):
        accel = str(round(uniform(0.5, 3.0), 1))
        decel = str(round(uniform(4.0, 6.0), 1))
        id = 'Car'+str(i)
        length = str(round(uniform(10, 25), 1))
        maxSpeed = str(randint(60, 120))
        sigma = '0.0'
        vType = SubElement(
            routes, 'vType', {'accel':accel, 'decel':decel, 'id':id, 'length':length, 'maxSpeed':maxSpeed, 'sigma':sigma})

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
        route = 'route'+str(i)
        type = "Car"+str(randint(0,num_vehicle_types))
        flow = SubElement(
            routes, 'flow',
            {'begin':begin, 'departPos':departPos, 'id':id, 'period':period, 'number':number, 'route':route, 'type':type})

    tree = ET.ElementTree(routes)
    tree.write(file_name + ".rou.xml")

    xml_ = xml.dom.minidom.parseString(tostring(routes))
    print(xml_.toprettyxml())

def all_xmls(graph, paths, num_vehicle_types, num_cars, file_name):
    nodes_xml(graph, paths, file_name)
    if type(paths[0]) == int:
        single_edges_xml(paths, file_name)
        single_route_vehicles_xml(paths, num_vehicle_types, num_cars, file_name)
    else:
        multiple_edges_xml(paths, file_name)
        multiple_route_vehicles_xml(paths, num_vehicle_types, num_cars, file_name)





























