import random
import string

from graphviz import Digraph

from controllers.classes.vertex import vertex
from controllers.data_structure.Linked_list import linked_list
from controllers.data_structure.adyance_list import adjacency_list
from controllers.classes.routes import routes
from controllers.data_structure.path_logaritme import shortest_path
from controllers.classes.vehicles import vehicles
from controllers.data_structure.path_logaritme import path
from controllers.nodes.linked_node import linked_node


class trips:

    def __init__(self, origin, destination, start_time, client, vehicle:vehicles, adyance_l):
        self.adjacency:adjacency_list = adyance_l
        self.id = self.generate_id()

        path_finder = shortest_path(adyance_l)
        path_route:path = path_finder.find_shortest_path(origin, destination)

        self.distance = path_route.distance
        self.origin = origin
        self.destination = destination
        self.start_time = start_time
        self.client = client
        self.vehicle = vehicle
        self.route_take:linked_list = path_route.path
        self.cost_trip = self.calculate_cost(vehicle.price, path_route.distance)

    def generate_id(self, length = 5) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def calculate_cost(self, vehicle_second_cost: float, total_distance: int):
        return vehicle_second_cost * total_distance

    def generate_graph(self):
        dot = Digraph()

        current:linked_node = self.route_take.head

        while current and current.next:
            print(current.value.value)
            start = current.value.value
            end = current.next.value.value
            distance = current.value.wide
            label = f'{start} -> {end}\nDistancia: {distance}'
            dot.node(start, start)
            dot.node(end, end)
            dot.edge(start, end, label)
            current = current.next

        dot.render(f'src/route_graph_{self.id}', format='png', cleanup=True, view=True)