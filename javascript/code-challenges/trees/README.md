# Trees

Implement a Node, a Binary Tree, and a Binary Search Tree.

## Challenge

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Create a Binary Tree class with preOrder, inOrder, and postOrder methods.

Create a Binary Search Tree that is a subclass of your Binary Tree that adds a new node in the correct location of the BST.

Add a method to the BST that takes a value in as an arguement and returns a boolean based on whether or not that value is found in the BST.

## Approach & Efficiency

For Binary Tree - used an empty tree array to push all nodes into this array (based on order) and return that array.

For Binary Search Tree I used a while loop that sets and places the value of new nodes in their correct location by comparing them to the value of previous nodes/node parents.
