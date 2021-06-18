class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def preorder(self):
        def preorder(root):
            if root is None:
                pass
            else:
                print(root.data,end=" ")
                preorder(root.left)
                preorder(root.right)
        preorder(self.root)

    def inorder(self):
        def inorder(root):
            if root is None:
                pass
            else:
                inorder(root.left)
                print(root.data, end=" ")
                inorder(root.right)
        inorder(self.root)

    def postorder(self):
        def postorder(root):
            if root is None:
                pass
            else:
                postorder(root.left)
                postorder(root.right)
                print(root.data, end=" ")
        postorder(self.root)

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BTree()

for i in array:
    bst.insert(i)

print('preorder:', end=" ")
bst.preorder()
print()

print('inorder:', end=" ")
bst.inorder()
print()

print('postorder:', end=" ")
bst.postorder()
print()


print()
print(bst.find(4))
