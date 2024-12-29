from graphviz import Source
from controllers.classes.routes import routes
from controllers.data_structure.Linked_list import linked_list
from controllers.classes.vertex import vertex
from controllers.nodes.linked_node import linked_node


class test:
    def __init__(self):
        lista_de_nodos:list = []
        accumulate=0;

class adjacency_list:
    def __init__(self):
        self.vertices: linked_list = linked_list()

    def add_vertex(self, route: routes):
        origin: vertex = vertex(route.origin)
        destine: vertex = vertex(route.destination)
        find_orign: linked_node = self.vertices.search(origin)
        if find_orign is not None:
            find_orign.value.edges.insert_final(destine, route.time)
        else:
            find_orign = self.vertices.insert_final(origin)
            find_orign.value.edges.insert_final(destine, route.time)

    def shortest_route(self):
        aux: linked_node = self.vertices.head

    def print(self):
        dot = 'digraph G {\n\tbgcolor="#1a1a1a"\n\tedge [arrowhead=none fontcolor=white color="#ff5400"];\n\t nodesep=0\n\t';
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white ';
        dot += 'color=transparent];\n\t';

        aux: linked_node = self.vertices.head

        while aux is not None:
            if aux is not None:
                dot += str(aux.value)
            aux = aux.next

        dot += "}"

        src = Source(dot, engine="neato")
        src.render("adyance", "./src", format="pdf", view=True)
        src.render("adyance", "./src", format="png", view=True)
