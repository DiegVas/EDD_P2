from controllers.classes.vehicles import vehicles


class BTreeNode:
    def __init__(self, leaf: bool = False):
        self.leaf: bool = leaf
        self.keys: list[vehicles] = []
        self.children: list[BTreeNode] = []

    def __str__(self):
        return f"Hoja: {self.leaf} - Keys: {self.keys} - Children: {self.children}"
