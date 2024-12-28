from controllers.nodes.linked_node import linked_node
from controllers.classes.vertex import vertex


class linked_list():
    def __init__(self):
        self.head: linked_node = None

    def insert_final(self, value: vertex, wed:int=0) -> linked_node:
        aux: linked_node = self.head
        value.wide = wed
        if aux is None:
            aux = linked_node(value);
            self.head = aux
            return self.head

        while aux.next is not None:
            aux = aux.next

        aux.next = linked_node(value)

        return aux.next

    def search(self, value: vertex) -> linked_node:
        temp: linked_node = self.head
        if temp is None:
            return None
        while temp is not None:
            if temp.value.value == value.value:
                return temp
            temp = temp.next
        return None
