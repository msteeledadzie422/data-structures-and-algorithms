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

  findMax() {
    let max = this.root.value;
    const traverse = (node) => {
      if (node.left) traverse(node.left);
      if(node.value > max){max = node.value};
      if (node.right) traverse(node.right);
    };
    traverse(this.root);
    return max;
  }
}

let tree = new BinaryTree();
tree.root = new Node(10);
tree.root.left = new Node(5);
tree.root.right = new Node(15);
tree.root.left.left = new Node(1);
tree.root.left.right = new Node(8);
tree.root.right.right = new Node(17);

tree.findMax();
