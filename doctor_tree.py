class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        new_node = DoctorNode(doctor_name)

        if self.root is None:
            print("Tree is empty, cannot insert without root.")
            return
        
        parent_node = self._find(self.root, parent_name)
        if parent_node is None:
            print(f"Parent {parent_name} not found, cannot insert {doctor_name}.")
            return
        
        if side == "left":
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                print(f"Left report of {parent_name} already exists.")
        elif side == "right":
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                print(f"Right report of {parent_name} already exists.")
        else:
            print(f"Invalid side {side}, use 'left' or 'right'.")

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node

        left_result = self._find(node.left, name)
        if left_result:
            return left_result

        return self._find(node.right, name)

    #Traversal Methods

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


#Testing Code
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    tree.insert("Dr. Nonexistent", "Dr. Who", "left")
    tree.insert("Dr. Croft", "Dr. Strange", "middle")
    tree.insert("Dr. Croft", "Dr. Brown", "left") 