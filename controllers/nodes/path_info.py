class path_info:
    def __init__(self, node_value: str, distance: int, previous: str):
        self.node_value = node_value
        self.distance = distance
        self.previous = previous
        self.next = None

