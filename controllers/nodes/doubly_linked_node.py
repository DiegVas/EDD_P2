from controllers.classes.client import client


class Node:
    def __init__(self, client_value: client):
        self.client = client_value
        self.next = None
        self.prev = None
