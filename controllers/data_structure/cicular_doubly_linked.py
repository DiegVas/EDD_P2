from controllers.nodes.doubly_linked_node import Node
from graphviz import Digraph
from controllers.classes.client import client


class circular_doubly_linked:
    def __init__(self):
        self.head = None

    def insert(self, new_client: client):
        new_node = Node(new_client)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            current = self.head
            while current.next != self.head and current.next.client.dpi < new_client.dpi:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            if current == self.head and new_client.dpi < self.head.client.dpi:
                self.head = new_node

    def __delete__(self, client_remove: client):
        current = self.head
        while current.next != self.head and current.client.dpi != client_remove.dpi:
            current = current.next
        if current.client.dpi == client_remove.dpi:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
            del current
        else:
            # ! Cliente no encontrado
            print("Client not found")

    def search(self, dpi: int) -> client:
        current = self.head
        while current.next != self.head and current.client.dpi != dpi:
            current = current.next
        if current.client.dpi == dpi:
            return current.client
        else:
            # ! Cliente no encontrado
            print("Client not found")
            return None

    def update(self, new_client: client):
        # ! No esta permitido modificar el dpi
        current = self.head
        while current.next != self.head and current.client.dpi != new_client.dpi:
            current = current.next
        if current.client.dpi == new_client.dpi:
            current.client = new_client
        else:
            # ! Cliente no encontrado
            print("Client not found")

    def display_graph(self):
        if self.head is None:
            print("Empty list")
            return
        current = self.head
        dot = Digraph(comment="Lista circular doblemente enlazada de los clientes")
        dot.attr(rankdir="LR")

        while True:
            dot.node(str(current.client.dpi), f'{current.client.name} ({current.client.dpi})')
            dot.edge(str(current.client.dpi), str(current.next.client.dpi), constraint='true')
            dot.edge(str(current.client.dpi), str(current.prev.client.dpi), constraint='true', _dir='back')
            current = current.next
            if current == self.head:
                break

        dot.render('circular_doubly_linked_list', "./src", format='png', view=True)

    def display(self):
        print("Circular Doubly Linked List:")
