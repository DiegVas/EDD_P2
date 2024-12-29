from controllers.nodes.trip_linked_node import trip_linked_node
from controllers.classes.client import client
from controllers.classes.trips import trips

class trip_linked_linked:
    def __init__(self):
        self.head:trip_linked_node = None

    def insert(self, value: trips):

        new_node = trip_linked_node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, value: str) -> trips:
        current = self.head
        while current:
            if current.value.id == value:
                return current.value
            current = current.next
        return None

    def delete(self, value: str):
        current = self.head
        if current.value.id == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value.id == value:
                current.next = current.next.next
                return
            current = current.next
        return

    def generate_dot_string(linked_list):
        dot_string = "digraph G {\n"
        dot_string += "  node [shape=record];\n"

        current = linked_list.head
        while current:
            dot_string += f'  "{current.value.id}" [label="{{<f0> {current.value.id} | <f1>}}"];\n'
            if current.next:
                dot_string += f'  "{current.value.id}":f1 -> "{current.next.value.id}":f0;\n'
            current = current.next

        dot_string += "}\n"
        return dot_string