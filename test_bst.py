import unittest
from BST import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Create a new Binary Search Tree before each test."""
        self.bst = BinarySearchTree()
       

    def test_insert_and_inorder_traversal(self):
        """Test inserting elements and checking in-order traversal."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.assertEqual(self.bst.inorder_traversal(self.bst.root), [2, 5, 7, 10, 15])

    def test_search(self):
        """Test searching for elements in the BST."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertTrue(self.bst.search(self.bst.root), 10)
        self.assertTrue(self.bst.search(self.bst.root), 5)
        self.assertFalse(self.bst.search(self.bst.root), 20)

    def test_preorder_traversal(self):
        """Test pre-order traversal."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.assertEqual(self.bst.preorder_traversal(self.bst.root), [10, 5, 2, 7, 15])

    def test_postorder_traversal(self):
        """Test post-order traversal."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.assertEqual(self.bst.postorder_traversal(self.bst.root), [2, 7, 5, 15, 10])

    def test_delete_leaf_node(self):
        """Test deleting a leaf node (node with no children)."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.bst.delete(self.bst.root, 2)
        self.assertEqual(self.bst.inorder_traversal(self.bst.root), [5, 7, 10, 15])

    def test_delete_node_with_one_child(self):
        """Test deleting a node with one child."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.delete(self.bst.root, 5)
        self.assertEqual(self.bst.inorder_traversal(self.bst.root), [2, 10, 15])

    def test_delete_node_with_two_children(self):
        """Test deleting a node with two children."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(7)
        self.bst.delete(self.bst.root, 5)
        self.assertEqual(self.bst.inorder_traversal(self.bst.root), [2, 7, 10, 15])

if __name__ == '__main__':
    unittest.main()
