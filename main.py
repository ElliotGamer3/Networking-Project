from src.network.presets.network1 import Network1
from src.network.presets.network2 import Network2
from src.simulation.scenarios.predictiveTravelerScenario import PredictiveTravelerScenario
from src.simulation.scenarios.nonPredictiveTravelerScenario import NonPredictiveTravelerScenario

from sys import setrecursionlimit as sysRL
sysRL(10000)


def main():

    networkPresets = {
        "network1": Network1,
        "network2": Network2
    }

    scenarioPresets = {
        "predictive": PredictiveTravelerScenario,
        "nonPredictive": NonPredictiveTravelerScenario
    }

    for presetName, networkPreset in networkPresets.items():  # for each network preset
        for scenarioName, scenarioPreset in scenarioPresets.items():  # run each scenario
            print("===============================================")
            print(f"Running {presetName} with {scenarioName} scenario")
            print("===============================================")
            network = networkPreset()  # create the network
            # create the scenario
            scenario = scenarioPreset(network, 100)  # 100 iterations
            scenario.run()
            print("===============================================")

    return 0


if __name__ == "__main__":
    main()
