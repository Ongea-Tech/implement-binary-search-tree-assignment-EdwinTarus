class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None
     
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        """Insert a value into the BST."""

        if not root:
            return TreeNode(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)
        return root 
        

    
    def search(self, root, value):
        """Search for a value in the BST. Return True if found, else False."""
        if root is None:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)
    
    def inorder_traversal(self, root):
        result = []
        if root:
            result.extend(self.inorder_traversal(root.left))
            result.append(root.value)
            # print(root.value, end = " ")
            result.extend(self.inorder_traversal(root.right))
        return result
    
    def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.value)
            result.extend(self.preorder_traversal(root.left))
            result.extend(self.preorder_traversal(root.right))
        return result
    
    def postorder_traversal(self, root):
        """Return a list of values representing post-order traversal."""
        result = []
        if root:
            result.extend(self.postorder_traversal(root.left))
            result.extend(self.postorder_traversal(root.right))
            result.append(root.value)
        return result 
    
    def delete(self, root, value):
        """Delete a value from the BST."""
        if not root:
            return root
        
        if value < root.value:
            root.left = self.delete(root.left, value)

        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            current = root.right
            while current.left:
                current = current.left
            root.value  = current.value
            root.right = self.delete(root.right, root.value)
        return root

    
# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(bst.root, 10))  # Expected output: True
print(bst.inorder_traversal(bst.root))  # Expected output: [5, 10, 15]
bst.delete(bst.root, 5)
print(bst.inorder_traversal(bst.root))
