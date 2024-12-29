from GUI.app import ModernDashboard
from controllers.classes.client import client
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.data_structure.b_tree import bTree
from controllers.data_structure.adyance_list import adjacency_list
from controllers.data_structure.trip_linked_linked import trip_linked_linked

if __name__ == "__main__":

    # ! Esctructuras de datos
    # Lista doblemente enlazada circular
    clients = circular_doubly_linked()
    # Árbol B
    vehicles_tree = bTree(5)
    # Lista de adyacencia
    adjacency = adjacency_list()
    # Lista enlazada de viajes
    trips = trip_linked_linked()



    app = ModernDashboard(clients, vehicles_tree, adjacency, trips)
    app.mainloop()
