from GUI.app import ModernDashboard
from controllers.classes.client import client
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.data_structure.b_tree import bTree
from controllers.data_structure.adyance_list import adjacency_list

if __name__ == "__main__":

    # ! Esctructuras de datos
    # Lista doblemente enlazada circular
    clients = circular_doubly_linked()
    #clients.insert(client(12345, "Juan", "Perez", "12345678", 13213,"aa"))
    # Árbol B
    vehicles_tree = bTree(5)
    # Lista de adyacencia
    adjacency = adjacency_list()

    app = ModernDashboard(clients, vehicles_tree, adjacency)
    app.mainloop()
