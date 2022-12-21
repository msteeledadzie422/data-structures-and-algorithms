'use strict';

function breadthFirst(tree) {
  let traversal = [];
  let breadthValues = [];
  traversal.push(tree.root);

  while (traversal.length > 0) {
    let current = traversal.shift();
    breadthValues.push(current);

    if (current.left) {
      traversal.push(current.left);
    }

    if (current.right) {
      traversal.push(current.right);
    }
    return breadthValues;
  }
}
