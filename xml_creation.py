from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.ElementTree as ET
import xml.dom.minidom


def nodes_xml(graph, path):
    '''
    Create xml file with nodes of a particular path (route)
    :return:
    '''

    nodes = Element('nodes')
    for node in path:
        id = str(node)
        coords = graph.node[node]['coordinate']
        x = str(coords[0])
        y = str(coords[1])
        node = SubElement(nodes, 'node', {'id': id, 'x': x, 'y': y})
    tree = ET.ElementTree(nodes)
    tree.write("project.nod.xml")

    xml_ = xml.dom.minidom.parseString(tostring(nodes))
    print xml_.toprettyxml()


def edges_xml(path):
    '''
    Create xml file with nodes of a particular path (route)
    :return:
    '''

    edges = Element('edges')
    first = path[0]
    for i in range(1, len(path)):
        from_ = str(first)
        to_ = str(path[i])
        id = from_+'_'+to_
        first = path[i]
        edge = SubElement(edges, 'edge', {'from': from_, 'id': id, 'to': to_})
    tree = ET.ElementTree(edges)
    tree.write("project.edg.xml")

    xml_ = xml.dom.minidom.parseString(tostring(edges))
    print xml_.toprettyxml()


def nodes_edges_to_xml(graph, path):
    nodes_xml(graph, path)
    edges_xml(path)