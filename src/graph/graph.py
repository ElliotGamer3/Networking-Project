from src.graph.graphable.graphable import Graphable
from src.graph.node.node import Node
from src.graph.edge.edge import Edge


class Graph:
    # connections is a dict of named edges and directed edges
    # {edge_name1: Edge, edge_name2: DirectedEdge}
    def __init__(self, graphable_elements: list[Graphable] = None) -> None:
        # initialize the graph with the connections
        # graph is a dict of edges and nodes { id: ("edge", Edge), id: ("node", Node), id: ("directed_edge", DirectedEdge)}
        self.graph = {}
        if graphable_elements is None:
            graphable_elements = []
        for element in graphable_elements:
            self.addElement(element)  # add the element to the graph

############################################################################################################
# Graph Methods                                                                                            #
############################################################################################################

    # adds a graphable element to the graph
    def addElement(self, element: Graphable) -> None:
        self.graph[element.guid] = (element.type, element)

    # removes a graphable element from the graph and returns it
    def removeElement(self, element: Graphable) -> Graphable:
        if element.guid not in self.graph.keys():
            raise ValueError("Element {element} does not exist in graph")
        return self.graph.pop(element.guid)

    # returns if an element is in the graph : NOT TESTED
    def contains(self, element: Graphable) -> bool:
        return element.guid in self.graph.keys()

    def getGraph(self) -> dict[str:Graphable]:
        return self.graph

    def getJSON(self) -> dict:
        graph = {}
        for graphable_element_guid, graphable_element in self.graph.items():
            graph[graphable_element_guid] = graphable_element.getJSON()
        return graph

    def __str__(self) -> str:
        rstr = ""
        for id, element in self.getGraph().items():
            rstr += f"id: {id}\nelement: {element}\n"
        return rstr

    def __repr__(self) -> str:
        return self.__str__()

    # returns a list of elements in the graph
    def getElementsString(self) -> str:
        rstr = ""
        for t, element in self.graph.values():
            rstr += f"{t}: {element}\n"
        return rstr

    # returns a list of the elements ids in the graph
    def getIdsString(self) -> str:
        rstr = ""
        for id in self.graph.keys():
            rstr += f"{id}\n"
        return rstr

############################################################################################################
# Node methods (These refer to nodes with no connections)                                                  #
############################################################################################################

    # adds a node to the graph
    def addNode(self, node: Node) -> None:
        self.graph[node.guid] = ("node", node)

    # remove the node from the graph and return it
    def removeNode(self, node: Node) -> Node:
        if node.guid not in self.graph.keys():
            raise ValueError("Node {node} does not exist in graph")
        return self.graph.pop(node.guid)

    # returns the node with the given name
    def getNode(self, name: str) -> Node:
        for t, node in self.graph.values():
            if node.name == name:
                return node
        # if the node is not found, raise an error
        raise ValueError("Node {name} does not exist in graph")

    # returns the node with the given GUID
    def getNodeByGUID(self, guid: str) -> Node:
        for t, node in self.graph.values():
            if node.guid == guid:
                return node
        # if the node is not found, raise an error
        raise ValueError("Node {guid} does not exist in graph")

    # get a list of nodes in the graph
    def getNodes(self) -> list[Node]:
        nodes = []  # create a list of nodes
        for t, element in self.graph.values():
            if isinstance(element, Node):  # if the element is a node
                nodes.append(element)  # add the node to the list
        return nodes  # return the list of nodes

    #returns the neighbors of a node that can be reached from an edge
    def getNeighbors(self, node: Node) -> list[Node]:
        neighbors = []
        for edge in self.getEdgesFromNode(node):
            neighbors.append(edge.getOtherNode(node))
        return neighbors

############################################################################################################
# Edge methods                                                                                             #
############################################################################################################

    # add an edge to the graph


    def addEdge(self, edge: Edge) -> None:
        # add an edge to the graph
        # if the edge is already in the graph
        if edge in self.getEdges():
            # raise an error
            raise ValueError("Edge {edge} already exists in graph")
        self.graph[edge.guid] = ("edge", edge)  # add the edge to the graph

    # remove an edge from the graph and return it

    def removeEdge(self, edge: Edge) -> Edge:
        for t, current_edge in self.graph.values():  # for each edge in the graph
            if current_edge == edge:
                return self.graph.pop(current_edge.guid)
        raise ValueError("Edge {edge} does not exist in graph")

    # returns the edge with the given name
    def getEdge(self, name: str) -> Edge:
        for t, edge in self.graph.values():
            if edge.name == name:
                return edge
        # if the edge is not found, raise an error
        raise ValueError("Edge {name} does not exist in graph")

    # returns the edge with the given GUID
    def getEdgeByGUID(self, guid: str) -> Edge:
        for t, edge in self.graph.values():
            if edge.guid == guid:
                return edge
        # if the edge is not found, raise an error
        raise ValueError("Edge {guid} does not exist in graph")

    # returns the edge based on another edge
    def getEdgeByEdge(self, edge: Edge) -> Edge:
        for t, current_edge in self.graph.values():
            if current_edge == edge:
                return current_edge
        # if the edge is not found, raise an error
        raise ValueError("Edge {edge} does not exist in graph")

    # returns the edge based on the nodes it connects and the direction
    def getEdgeByNodes(self, node1: Node, node2: Node) -> Edge:
        #check if an edge exists between the two nodes
        for t, edge in self.graph.values():
            if edge.node1 == node1 and edge.node2 == node2:
                return edge
            if edge.node1 == node2 and edge.node2 == node1:
                return edge
        # if the edge is not found, raise an error
        raise ValueError(
            "Edge connecting {node1} and {node2} does not exist in graph")

    # returns a list of edges in the graph
    def getEdges(self) -> list[Edge]:
        edges = []
        for t, element in self.graph.values():
            if isinstance(element, Edge):
                edges.append(element)
        return edges

    # returns a list of edges that connect to the given node going out of the node
    def getEdgesFromNode(self, node: Node) -> list[Edge]:
        edges = []  # create a list of edges
        for edge in self.getEdges():  # for each edge in the graph
            # if the edge connects to the node and is not a directed edge going into the node
            if (edge.node1 == node and not edge.direction == -1) or (edge.node2 == node and not edge.direction == 1):
                edges.append(edge)  # add the edge to the list
        return edges  # return the list of edges
