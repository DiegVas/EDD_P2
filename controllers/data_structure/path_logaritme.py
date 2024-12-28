from controllers.classes.vertex import vertex
from controllers.data_structure.Linked_list import linked_list
from controllers.nodes.path_info import path_info


class path_list:
    def __init__(self):
        self.head = None

    def insert(self, node_value: str, distance: int, previous: str):
        new_node = path_info(node_value, distance, previous)
        if self.head is None:
            self.head = new_node
            return

        if new_node.distance < self.head.distance:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.distance <= new_node.distance:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def get_min(self):
        if self.head is None:
            return None
        min_node = self.head
        self.head = self.head.next
        return min_node

    def contains(self, value: str) -> bool:
        current = self.head
        while current:
            if current.node_value == value:
                return True
            current = current.next
        return False


class shortest_path:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

    def find_shortest_path(self, start: str, end: str):
        # Inicializar estructuras
        unvisited = path_list()
        path_tracker = path_list()

        # Inicializar el nodo de inicio
        unvisited.insert(start, 0, "")

        while True:
            current = unvisited.get_min()
            if current is None:
                return None, None  # No hay camino

            # Guardar información del camino
            path_tracker.insert(current.node_value, current.distance, current.previous)

            if current.node_value == end:
                return self._get_path(path_tracker, start, end), current.distance

            # Obtener el vértice actual
            current_vertex = self._find_vertex(current.node_value)
            if current_vertex is None:
                continue

            # Explorar vecinos
            edge = current_vertex.edges.head
            while edge:
                neighbor_value = edge.value.value
                if not path_tracker.contains(neighbor_value):
                    new_distance = current.distance + edge.value.wide
                    unvisited.insert(neighbor_value, new_distance, current.node_value)
                edge = edge.next

    def _find_vertex(self, value: str):
        current = self.graph.vertices.head
        while current:
            if current.value.value == value:
                return current.value
            current = current.next
        return None

    def _get_path(self, path_tracker: path_list, start: str, end: str):
        result = linked_list()
        current_value = end

        while current_value != start:
            current = path_tracker.head
            while current:
                if current.node_value == current_value:
                    result.insert_final(vertex(current_value))
                    current_value = current.previous
                    break
                current = current.next

        result.insert_final(vertex(start))

        # Invertir la lista para tener el camino en orden correcto
        reversed_path = linked_list()
        current = result.head
        while current:
            temp_vertex = vertex(current.value.value)
            reversed_path.insert_final(temp_vertex)
            current = current.next

        return reversed_path

    def print_path(self, path: linked_list, distance: int):
        if not path:
            print("No se encontró un camino")
            return

        result = ""
        current = path.head
        while current:
            result += current.value.value
            if current.next:
                result += " -> "
            current = current.next

        print(f"Camino más corto: {result}")
        print(f"Distancia total: {distance}")


