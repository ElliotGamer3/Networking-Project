# class for a generic network
class GenericNetwork:
    def __init__(self, network) -> None:
        self.network = network


class GenericNetworkWithTravelers:
    def __init__(self, network, travelers) -> None:
        self.network = network
        self.travelers = travelers

    def tick(self) -> None:
        for traveler in self.travelers:
            traveler.goToNext()
