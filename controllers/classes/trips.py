import random
import string
from controllers.classes.vertex import vertex
from controllers.data_structure.Linked_list import linked_list
from controllers.data_structure.adyance_list import adjacency_list
from controllers.classes.routes import routes
from controllers.data_structure.path_logaritme import shortest_path
from controllers.classes.vehicles import vehicles

class trips:

    def __init__(self, origin, destination, start_time, client, vehicle:vehicles, adyance_l):
        self.adjacency:adjacency_list = adyance_l
        self.id = self.generate_id()

        path_finder = shortest_path(adyance_l)
        path = path_finder.find_shortest_path(origin, destination)

        self.origin = origin
        self.destination = destination
        self.start_time = start_time
        self.client = client
        self.vehicle = vehicle
        self.route_take = path.path
        self.cost_trip = self.calculate_cost(vehicle.price, path.distance)

    def generate_id(self, length = 5) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def calculate_cost(self, vehicle_second_cost: int, total_distance: int):
        return vehicle_second_cost * total_distance