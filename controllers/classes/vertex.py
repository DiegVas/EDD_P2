class vertex:
    def __init__(self, value, wide: int = 0):
        self.value: str = value
        self.edges = self._initialize_edges()
        self.wide: int = wide
        self.accumulated_weight: int = 0
        self.visited = False

    def _initialize_edges(self):
        from controllers.data_structure.Linked_list import linked_list
        return linked_list()

    def increase_wight(self, weight: int) -> int:
        self.accumulated_weight += weight
        return self.accumulated_weight

    def __str__(self) -> str:
        aux = self.edges.head

        dot: str = ""

        while aux is not None:
            dot += f'edge[label={aux.value.wide} fontsize=5];\n\t{self.value} -> {aux.value.value};\n\t';

            aux = aux.next

        return dot
