'use strict';

const BinaryTree = require('./index');

describe('Tree function', () => {
  test('Can successfully instantiate an empty tree', () => {
    let tree = new BinaryTree();
    expect(tree).toEqual({});
  });
  test('Can successfully instantiate a tree with a single root node', () => {
    let tree = new BinaryTree();
    tree.root = new Node(10);
    expect(tree.root.value).toEqual(10);
  });
  test('For a Binary Search Tree, can successfully add a left child and right child properly to a node', () => {
    let tree = new BinaryTree();
    tree.root = new Node(10);
    tree.root.left = new Node(5);
    tree.root.right = new Node(15);
    expect(tree.root.left.value).toEqual(5);
    expect(tree.root.right.value).toEqual(15);
  });
});
