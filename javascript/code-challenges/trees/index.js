'use strict';

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
  }

  preOrder() {
    const tree = [];
    const traverse = (node) => {
      tree.push(node.value);
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
    };
    traverse(this.root);
    console.log(tree);
  }

  inOrder(){
    const tree = [];
    const traverse = (node) => {
      if (node.left) traverse(node.left);
      tree.push(node.value);
      if (node.right) traverse(node.right);
    };
    traverse(this.root);
    console.log(tree);
  }

  postOrder(){
    const tree = [];
    const traverse = (node) => {
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
      tree.push(node.value);
    };
    traverse(this.root);
    console.log(tree);
  }
}

class BinarySearchTree extends BinaryTree {
  constructor() {
    super();
  }

  add(value) {
    let currentNode = new Node(value);

    this.root = currentNode;

    while (currentNode) {
      if (value < currentNode.value) {
        if (currentNode.left === null) {
          currentNode.left = new Node(value);
          currentNode = null;
        } else {
          currentNode = currentNode.left;
        }
      } else if (value > currentNode.value) {
        if (currentNode.right === null) {
          currentNode.right = new Node(value);
          currentNode = null;
        } else {
          currentNode = currentNode.right;
        }
      } else {
        throw new Error("Value already exists");
      }
    }
  }

  contains(value) {
    let currentNode = this.root;

    while (currentNode) {
      if (value === currentNode.value) {
        return true;
      } else if (value > currentNode.value) {
        currentNode = currentNode.right;
      } else {
        currentNode = currentNode.left;
      }
    }
    return false;
  }

}

let tree = new BinaryTree();
tree.root = new Node(10);
tree.root.left = new Node(5);
tree.root.right = new Node(15);
tree.root.left.left = new Node(1);
tree.root.left.right = new Node(8);
tree.root.right.right = new Node(17);

tree.preOrder();
tree.inOrder();
tree.postOrder();

let tree2 = new BinarySearchTree();
tree2.root = new Node(10);
tree2.root.left = new Node(5);
tree2.root.right = new Node(15);
tree2.root.left.left = new Node(1);
tree2.root.left.right = new Node(8);
tree2.root.right.right = new Node(17);

tree2.add();
