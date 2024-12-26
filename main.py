from GUI.app import ModernDashboard
from controllers.classes.client import client
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.data_structure.b_tree import bTree

if __name__ == "__main__":
    b_tree = bTree(5)

    for i in range(1, 11):
        b_tree.insert(i)

    b_tree.delete(b_tree.root, 3)
    b_tree.delete(b_tree.root, 6)
    b_tree.delete(b_tree.root, 7)
    b_tree.render_b_tree()
    print(b_tree.search_key(3))
