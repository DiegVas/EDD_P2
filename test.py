from controllers.classes.vertex import vertex
from controllers.data_structure.Linked_list import linked_list
from controllers.data_structure.adyance_list import adjacency_list
from controllers.classes.routes import routes
from controllers.data_structure.path_logaritme import shortest_path


def main():
    adjacency = adjacency_list()

    # Crear rutas (conexiones con pesos)
    routesList = [
        routes("1", "2", 4),
        routes("1", "3", 3),
        routes("2", "5", 8),
        routes("5", "7", 17),
        routes("7", "8", 9),
        routes("3", "4", 12),
        routes("4", "7", 20),
        routes("3", "6", 4),
        routes("4", "6", 2),
        routes("6", "8", 22),
        routes("4", "8", 15),

    ]

    # Agregar rutas a la lista de adyacencia
    for route in routesList:
        adjacency.add_vertex(route)

    path_finder = shortest_path(adjacency)
    # Encontrar el camino más corto
    path= path_finder.find_shortest_path("1", "2")

    # Imprimir el resultado
    path_finder.print_path(path.path, path.distance)


if __name__ == "__main__":
    main()
