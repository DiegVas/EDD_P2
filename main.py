from GUI.app import ModernDashboard
from controllers.classes.client import client
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.data_structure.b_tree import bTree
from controllers.classes.vehicles import vehicles
from controllers.data_structure.adyance_list import adjacency_list
from controllers.classes.vertex import vertex

if __name__ == "__main__":
    # b_tree = bTree(5)

    # b_tree.render_b_tree();

    adjacency = adjacency_list()
    vertex1 = vertex("1")
    vertex2 = vertex("2")
    vertex3 = vertex("3")
    vertex4 = vertex("4")
    vertex5 = vertex("5")
    vertex6 = vertex("6")
    adjacency.add_vertex(vertex1, vertex2)
    adjacency.add_vertex(vertex1, vertex3)
    adjacency.add_vertex(vertex1, vertex4)
    adjacency.add_vertex(vertex1, vertex5)

    adjacency.print()
