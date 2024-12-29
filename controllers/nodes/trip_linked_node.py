from controllers.classes.trips import trips


class trip_linked_node:
    def __init__(self, value: trips):
        self.value: trips = value
        self.next: trip_linked_node = None
