from graphviz import Source
from controllers.classes.vehicles import vehicles
from controllers.nodes.b_tree_node import BTreeNode


class bTree:
    def __init__(self, order: int):
        self.root = BTreeNode(True)
        self.order: int = order

    def insert(self, vehicle_value: vehicles):
        root = self.root
        self.insert_value_no_complete(root, vehicle_value)
        if len(root.keys) > self.order - 1:
            temp: BTreeNode = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)

    def insert_value_no_complete(self, root: BTreeNode, vehicle_value: vehicles):
        counter: int = len(root.keys) - 1
        if root.leaf:
            root.keys.append(None)
            while counter >= 0 and vehicle_value.plate < root.keys[counter].plate:
                root.keys[counter + 1] = root.keys[counter]
                counter -= 1
            root.keys[counter + 1] = vehicle_value
        else:
            while counter >= 0 and vehicle_value < root.keys[counter]:
                counter -= 1
            counter += 1
            self.insert_value_no_complete(root.children[counter], vehicle_value)
            if len(root.children[counter].keys) > self.order - 1:
                self.split_child(root, counter)

    def split_child(self, root_child: BTreeNode, i: int):
        i_middle: int = int((self.order - 1) / 2)
        child: BTreeNode = root_child.children[i]
        nodo_temp: BTreeNode = BTreeNode(child.leaf)
        root_child.children.insert(i + 1, nodo_temp)
        root_child.keys.insert(i, child.keys[i_middle])
        nodo_temp.keys = child.keys[i_middle + 1:i_middle * 2 + 1]
        child.keys = child.keys[0:i_middle]
        if not child.leaf:
            nodo_temp.children = child.children[i_middle + 1: i_middle * 2 + 2]
            child.children = child.children[0:i_middle + 1]

    def search_key(self, value: vehicles, root: BTreeNode = None):
        if root is not None:
            i = 0
            while i < len(root.keys) and value > root.keys[i]:
                i += 1
            if i < len(root.keys) and value == root.keys[i]:
                return root.keys[i]
            elif root.leaf:
                return None
            else:
                return self.search_key(value, root.children[i])

        else:
            return self.search_key(value, self.root)

    def render_b_tree(self):
        dot: str = "digraph G {\n\t"
        dot += "fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false\n\t"
        dot += 'node [shape=record width=1.2 style=filled fillcolor="#313638"'
        dot += "fontcolor=white color=transparent];\n\t"
        dot += 'edge [fontcolor=white color="#0070C9"];\n\t'
        dot += self.print_tree(self.root)
        dot += "\n}"
        src = Source(dot)
        src.render("b_tree", "./src", format="png", view=True)

    def print_tree(self, node: BTreeNode, id: list[int] = [0]) -> str:
        root: BTreeNode = node
        tree = f"n{id[0]}[label=\" "
        counter: int = 0

        for i in root.keys:
            if counter == len(root.keys) - 1:
                tree += f"<f{counter}>|{i.plate}|<f{counter + 1}>|"
                break
            tree += f"<f{counter}>|{i.plate}|"
            counter += 1

        tree += "\"];\n\t"

        counter = 0
        id_father = id[0]
        for i in root.children:
            tree += f"n{id_father}:f{counter} -> n{id[0] + 1};\n\t"
            id[0] += 1
            tree += self.print_tree(i, id)
            counter += 1

        return tree

    def delete_predecessor(self, node: BTreeNode):
        if node.leaf:
            return node.keys.pop()
        n = len(node.keys) - 1
        if len(node.children[n].keys) >= self.order:
            self.delete_sibling(node, n + 1, n)
        else:
            self.delete_merge(node, n, n + 1)
        return self.delete_predecessor(node.children[n])

    def delete_successor(self, node: BTreeNode):
        if node.leaf:
            return node.keys.pop(0)
        if len(node.children[1].keys) >= self.order:
            self.delete_sibling(node, 0, 1)
        else:
            self.delete_merge(node, 0, 1)
        return self.delete_successor(node.children[0])

    def delete(self, root: BTreeNode, value: vehicles):
        t = self.order
        i = 0
        # Encontrar la posición correcta del valor
        while i < len(root.keys) and value > root.keys[i]:
            i += 1

        # Si estamos en una hoja, simplemente eliminamos el valor si existe
        if root.leaf:
            if i < len(root.keys) and root.keys[i] == value:
                root.keys.pop(i)
            return

        # Si encontramos el valor en el nodo actual
        if i < len(root.keys) and root.keys[i] == value:
            self.delete_internal_node(root, value, i)
            return

        # Si el valor podría estar en uno de los hijos
        if i <= len(root.children) - 1:  # Verificamos que el índice sea válido
            if len(root.children[i].keys) >= t:
                self.delete(root.children[i], value)
            else:
                # Manejo de casos cuando el hijo tiene menos de t claves
                if i > 0 and len(root.children[i - 1].keys) >= t:
                    # Tomar prestado del hermano izquierdo
                    self.delete_sibling(root, i, i - 1)
                elif i < len(root.children) - 1 and len(root.children[i + 1].keys) >= t:
                    # Tomar prestado del hermano derecho
                    self.delete_sibling(root, i, i + 1)
                else:
                    # Fusionar con un hermano
                    if i > 0:
                        self.delete_merge(root, i, i - 1)
                    else:
                        self.delete_merge(root, i, i + 1)
                self.delete(root.children[i - 2], value)

    # Delete internal node
    def delete_internal_node(self, node: BTreeNode, value: vehicles, i):
        t = self.order
        if node.leaf:
            if node.keys[i] == value:
                node.keys.pop(i)
                return
            return

        if len(node.children[i].keys) >= t:
            node.keys[i] = self.delete_predecessor(node.children[i])
            return
        elif len(node.children[i + 1].keys) >= t:
            node.keys[i] = self.delete_successor(node.children[i + 1])
            return
        else:
            self.delete_merge(node, i, i + 1)
            self.delete_internal_node(node.children[i], value, self.order - 1)

    def delete_merge(self, node: BTreeNode, i: int, j: int):
        cnode = node.children[i]

        if j > i:
            # Case when merging with right sibling
            rsnode = node.children[j]
            cnode.keys.append(node.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.children) > 0:
                    cnode.children.append(rsnode.children[k])
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children.pop())
            new = cnode
            node.keys.pop(i)
            node.children.pop(j)
        else:
            # Case when merging with left sibling
            lsnode = node.children[j]
            lsnode.keys.append(node.keys[j])
            for k in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[k])
                if len(cnode.children) > 0:
                    lsnode.children.append(cnode.children[k])
            if len(cnode.children) > 0:
                lsnode.children.append(cnode.children.pop())
            new = lsnode
            node.keys.pop(j)
            node.children.pop(i)  # This was causing the issue

        # Update root if necessary
        if node == self.root and len(node.keys) == 0:
            self.root = new

    # Delete the sibling
    def delete_sibling(self, node: BTreeNode, i: int, j: int):
        cnode = node.children[i]
        if i < j:
            rsnode = node.children[j]
            cnode.keys.append(node.keys[i])
            node.keys[i] = rsnode.keys[0]
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children[0])
                rsnode.children.pop(0)
            rsnode.keys.pop(0)
        else:
            lsnode = node.children[j]
            cnode.keys.insert(0, node.keys[i - 1])
            node.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.children) > 0:
                cnode.children.insert(0, lsnode.children.pop())

    def __str__(self):
        return f"{self.root}"
