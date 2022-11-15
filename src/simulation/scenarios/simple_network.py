from src.graph.graph import Graph
from src.graph.node.node import Node
from src.graph.edge.edge import Edge
from src.graph.graphable.graphable import Graphable
from src.network.network import Network
from src.simulation.traveler import Traveler

# this class represents a simple network with 3 nodes and 2 edges
# the goal of the network is to travel from node1 to node3


class SimpleNetwork:
    def __init__(self) -> None:
        # create the nodes
        self.node1 = Node("node1")
        self.node2 = Node("node2")
        self.node3 = Node("node3")
        # create the edge between the nodes with a cost of 1
        self.edge = Edge(self.node1, self.node2, 1, "edge1", 1.0)
        self.edge = Edge(self.node2, self.node3, 1, "edge2", 1.0)
        # save the network name
        self.name = "simple_network"
        # create the network with the nodes and edges
        self.network = Network([self.node1, self.node2, self.edge])

class TravelClass(SimpleNetwork):
    def __init__(self) -> None:
        super().__init__()
        self.travelers = [Traveler(
            self.network, "traveler1", self.node1, self.node3)]
        self.last_travel_paths = []
        self.interaction_cost_log = []
        self.complete_system_cost_log = []
        self.system_cost_log = []
        self.travel_path_log = []
        self.total_ticks = 0

    # function for performing a tick of the simulation (override this in the travel class)
    def tick(self) -> None:
        self.total_ticks += 1

    def log(self) -> None:
        self.interaction_cost_log.append(self.network.getInteractionCosts(self.last_travel_paths))
        # log the complete system cost
        self.complete_system_cost_log.append(self.network.getCompleteSystemCost())
        # log the system cost
        self.system_cost_log.append(self.network.getSystemCost())
        # log the travel path
        self.travel_path_log.append(self.last_travel_paths)

    def printLogs(self) -> None:
        #print out all the logs for the travelers
        for tick in range(self.total_ticks):
            print("Tick: " + str(tick))
            print("Interaction Cost: " + str(self.interaction_cost_log[tick]))
            print("Complete System Cost: " + str(self.complete_system_cost_log[tick]))
            print("System Cost: " + str(self.system_cost_log[tick]))
            print("Travel Path: " + str(self.travel_path_log[tick]))
            print("")

#travel class that travels to all nodes in the network
class EveryNodeTravel(TravelClass):
    # function for performing a tick of the simulation
    def tick(self) -> None:
        super().tick() # call the super class tick function
        #below is the travel method specific to this class
        # create a list of traveler's travel paths
        traveler_paths = []
        # perform a tick for each traveler and save their travel path
        for traveler in self.travelers:
            for neighbor in self.network.getNeighbors(traveler.start_location):
                subTraveler = Traveler(self.network, start_location=neighbor, end_location=traveler.end_location)
                traveler_paths.append(subTraveler.travelTo(neighbor))
        self.last_travel_paths = traveler_paths
        self.log()

if __name__ == "__main__":
    # create an instance of the travel class
    travel = EveryNodeTravel()
    # perform 10 ticks of the simulation
    for i in range(10):
        travel.tick()
    # print out the logs
    travel.printLogs()