import src.graph.graph as Graph
import src.graph.edge.edge as Edge
import src.graph.node.node as Node
from src.network.presets.network1 import Network1
from src.simulation.scenarios.predictiveTravelerScenario import PredictiveTravelerScenario
from src.simulation.scenarios.nonPredictiveTravelerScenario import NonPredictiveTravelerScenario

from sys import setrecursionlimit as sysRL
sysRL(10000)


def main():
    # create a scenario for basic goes to every node traveler
    scenario = NonPredictiveTravelerScenario(Network1())
    scenario.run()
    print(scenario.network.graph)
    print(scenario.getLogs())

    # create a new scenario for predictive scoring
    scenario2 = PredictiveTravelerScenario(Network1())
    scenario2.run()
    print(scenario2.network.graph)
    print(scenario2.getLogs())

    return 0


if __name__ == "__main__":
    main()
