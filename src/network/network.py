from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable

# This class defines a network
# a network is a set of nodes and edges in a graph
# it must must provide a method track the current costs of the network elements
# it must provide a method to update the network elements costs to a given set of costs
# it must provide a method to reset the network elements costs


class Network(Graph):
    # creates a network with the given nodes and edges
    def __init__(self, nodes: list[Node] = None, edges: list[Edge] = None) -> None:
        super().__init__(nodes + edges)
        # this represents the cost of each node for each to perform an interaction with a traveller
        self.node_costs = {}
        # this represents the cost of each edge to perform an interaction with a traveller
        self.edge_costs = {}
        self.reset()

    # creates a network with the given graphable elements
    def __init__(self, graphable_elements: list[Graphable] = None) -> None:
        super().__init__(graphable_elements)
        # this represents the cost of each node for each to perform an interaction with a traveller
        self.node_costs = {}
        # this represents the cost of each edge to perform an interaction with a traveller
        self.edge_costs = {}
        self.reset()

    # adds all of the nodes and edges costs to the network costs
    def reset(self) -> None:
        for node in self.getNodes():
            self.node_costs[node.guid] = node.cost
        for edge in self.getEdges():
            self.edge_costs[edge.guid] = edge.cost

############################################################################################################
# Node Getters
############################################################################################################

    # returns the current cost of the given node
    def getNodeCost(self, node: Node) -> float:
        # check if the node exists
        if node.guid not in self.node_costs.keys():
            raise ValueError(f"Node {node} does not exist in costs")
        return self.node_costs[node.guid]

    # returns the current cost of the given node with the given GUID
    def getNodeCostByGUID(self, guid: str) -> float:
        # check if the node exists
        if guid not in self.node_costs.keys():
            raise ValueError(f"Node {guid} does not exist in costs")
        return self.node_costs[guid]

    # returns the current cost of the given node with the given name
    def getNodeCostByName(self, name: str) -> float:
        for node in self.getNodes():
            if node.name == name:
                return self.node_costs[node.guid]
        raise ValueError(f"Node {name} does not exist in costs")

############################################################################################################
# Edge Getters
############################################################################################################

    # returns the current cost of the given edge
    def getEdgeCost(self, edge: Edge) -> float:
        # check if the edge exists
        if edge.guid not in self.edge_costs.keys():
            raise ValueError(f"Edge {edge} does not exist in costs")
        return self.edge_costs[edge.guid]

    # returns the current cost of the given edge with the given GUID
    def getEdgeCostByGUID(self, guid: str) -> float:
        # check if the edge exists
        edge = self.getEdgeByGUID(guid)
        if edge.guid not in self.edge_costs.keys():
            self.edge_costs[edge.guid] = 0.0
        return self.edge_costs[edge.guid]

    # returns the current cost of the given edge with the given name
    def getEdgeCostByName(self, name: str) -> float:
        edge = self.getEdge(name)
        if edge.guid not in self.edge_costs.keys():
            self.edge_costs[edge.guid] = 0.0
        return self.edge_costs[edge.guid]

############################################################################################################
# Node Setters
############################################################################################################

    # sets the current cost of the given node
    def setNodeCost(self, node: Node, cost: float) -> None:
        # check if the node exists
        if not self.contains(node):
            raise ValueError(f"Node {node} does not exist in graph")
        self.node_costs[node.guid] = cost

    # sets the current cost of the given node with the given GUID
    def setNodeCostByGUID(self, guid: str, cost: float) -> None:
        node = self.getNodeByGUID(guid)
        self.node_costs[node.guid] = cost

    # sets the current cost of the given node with the given name
    def setNodeCostByName(self, name: str, cost: float) -> None:
        node = self.getNode(name)
        self.node_costs[node.guid] = cost

############################################################################################################
# Edge Setters
############################################################################################################

    # sets the current cost of the given edge
    def setEdgeCost(self, edge: Edge, cost: float) -> None:
        # check if the edge exists
        if not self.contains(edge):
            raise ValueError("Edge {edge} does not exist in graph")
        self.edge_costs[edge.guid] = cost

    # sets the current cost of the given edge with the given GUID
    def setEdgeCostByGUID(self, guid: str, cost: float) -> None:
        edge = self.getEdgeByGUID(guid)
        self.edge_costs[edge.guid] = cost

    # sets the current cost of the given edge with the given name
    def setEdgeCostByName(self, name: str, cost: float) -> None:
        edge = self.getEdge(name)
        self.edge_costs[edge.guid] = cost

    # returns the current cost of the given network element
    def updateCost(self, guid: str, cost: float) -> None:
        if guid not in self.getGraph().keys():
            raise ValueError("Element {guid} does not exist in graph")
        # set element to the element with the given guid
        t, element = self.getGraph()[guid]
        if isinstance(element, Node):
            self.setNodeCostByGUID(element.guid, cost)
        elif isinstance(element, Edge):
            self.setEdgeCostByGUID(element.guid, cost)
        else:
            raise ValueError(
                "Element type {elementType} does not have a cost associated with it")

    # updates the network to the given set of costs for the network elements
    def updateCosts(self, new_costs: dict[str, float] = None) -> None:
        if new_costs == None:  # if no new costs are given
            return  # do nothing
        for guid in new_costs:
            self.updateCost(guid, new_costs[guid])

############################################################################################################

    # returns a dictionary of the costs of all network elements in the network
    # for a list of travel paths between all nodes in the network
    def getInteractionCosts(self, travel_paths: list[list[Node]]) -> dict[str, float]:
        interaction_costs = {}
        for path in travel_paths:
            if len(path) == 0:  # if the path is empty (no nodes)
                continue
            if len(path) == 1:  # if the path only contains one node
                interaction_costs[path[0].guid] = self.getNodeCost(path[0])
                continue
            for node in path[1:]:  # for all nodes except the first one
                prev_node = path[path.index(node) - 1]  # get the previous node
                # add the cost of the previous node to the calculated costs
                if prev_node.guid not in interaction_costs.keys():
                    interaction_costs[prev_node.guid] = 0.0
                interaction_costs[node.guid] = interaction_costs[prev_node.guid]
                interaction_costs[node.guid] += self.getNodeCost(node)
                # get the edge between the previous and the current node
                edge = self.getEdgeByNodes(prev_node, node)
                if edge.guid not in interaction_costs.keys():
                    interaction_costs[edge.guid] = 0.0
                interaction_costs[edge.guid] += self.getEdgeCost(edge)
        return interaction_costs

    # get the complete system cost which is the average of the node and edge costs
    def getCompleteSystemCost(self) -> float:
        return (sum(self.node_costs.values()) + sum(self.edge_costs.values())) / (len(self.node_costs) + len(self.edge_costs))

    # get the system cost for the given node
    def getNodeSystemCost(self, node: Node) -> float:
        nodeSystemCost = 0.0
        # add the cost of the node itself the edges connected to the node and the nodes connected to the node and return the average
        counter = 1
        nodeSystemCost += self.getNodeCost(node)
        for edge in self.getEdgesFromNode(node):
            counter += 2
            nodeSystemCost += self.getEdgeCost(edge)
            nodeSystemCost += self.getNodeCost(edge.getOtherNode(node))
        # return the average of the costs
        return nodeSystemCost / counter

    # get the system cost for the all nodes

    def getSystemCost(self) -> dict[str, float]:
        return {node.name: self.getNodeSystemCost(node) for node in self.getNodes()}
