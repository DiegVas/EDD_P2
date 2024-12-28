from graphviz import Source

from controllers.data_structure.Linked_list import linked_list
from controllers.classes.vertex import vertex
from controllers.nodes.linked_node import linked_node


class adjacency_list:
    def __init__(self):
        self.vertices: linked_list = linked_list()

    def add_vertex(self, orign: vertex, destine: vertex):
        find_orign: linked_node = self.vertices.search(orign)
        if find_orign is not None:
            find_orign.value.edges.insert(destine)
        else:
            find_orign = self.vertices.insert(orign)
            find_orign.value.edges.insert(destine)

    def print(self):
        dot = 'digraph G {\n\tbgcolor="#1a1a1a"\n\tedge [arrowhead=none fontcolor=white color="#ff5400"];\n\t';
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white ';
        dot += 'color=transparent];\n\t';

        aux: linked_node = self.vertices.head

        while aux is not None:
            if aux is not None:
                dot += str(aux.value)
            aux = aux.next

        dot += "}"

        src = Source(dot)
        src.render("b_tree", "./src", format="png", view=True)
