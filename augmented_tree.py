
class Node:
    def __init__(self, data = 0, n_childs = 2):
        self.data = data
        self.childs = [None] * n_childs

class Tree:
    def __init__(self, node, path = None):
        self.root = node
        if path is None:
            self.path = []
        else:
            self.path = path

    def printDFS(self):

        if not self.root.childs:
            print self.path
        else:
            for node_child in self.root.childs:
                tree_child = Tree(node_child, path = self.path + [node_child.data])
                tree_child.printDFS()

        return None

if __name__ == '__main__':
    a= Node(1, 3)
    a.childs[0] = Node(2, 2)
    a.childs[1] = Node(3, 2)
    a.childs[2] = Node(4, 1)

    a.childs[0].childs[0] = Node(5, 0)
    a.childs[0].childs[1] = Node(6, 0)
    a.childs[1].childs[0] = Node(7, 0)
    a.childs[1].childs[1] = Node(8, 0)
    a.childs[2].childs[0] = Node(9, 1)
    a.childs[2].childs[0].childs[0] = Node(10, 0)

    aTree = Tree(a, [a.data])
    aTree.printDFS()
