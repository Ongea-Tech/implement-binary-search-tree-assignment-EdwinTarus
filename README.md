[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QvYmL-S0)
# BSTTemplate
This is a Binary Search Tree template

# Binary Search Tree Assignment

## Overview
This assignment requires students to implement a Binary Search Tree (BST) in Python. The provided `bst_assignment.py` file contains a class definition with method stubs that need to be completed.

## Requirements
Students must implement the following methods:
- `insert(value)`: Insert a value into the BST.
- `search(value)`: Search for a value in the BST and return `True` if found, otherwise `False`.
- `inorder_traversal()`: Return a list of values using in-order traversal.
- `preorder_traversal()`: Return a list of values using pre-order traversal.
- `postorder_traversal()`: Return a list of values using post-order traversal.
- `delete(value)`: Remove a value from the BST.

## Running Tests
Unit tests are provided in `test_bst.py`. To run the tests, execute the following command:

```bash
python -m unittest test_bst.py
```

Alternatively, GitHub Classroom will automatically run tests using GitHub Actions. 

## Example Usage
```python
from bst_assignment import BinarySearchTree

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
print(bst.inorder_traversal())  # Expected output: [2, 5, 7, 10, 15]
```

## Submission
Submit your completed assignment `BST.py` file via GitHub Classroom. Ensure all methods are correctly implemented and that all tests pass before submission.
