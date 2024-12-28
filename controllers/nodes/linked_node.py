from controllers.classes.vertex import vertex


class linked_node:
    def __init__(self, value: vertex):
        self.value = value
        self.next: linked_node = None
