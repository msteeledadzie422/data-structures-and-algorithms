'use strict';

function tree_intersection(tree1,tree2) {

  let arr = [];

  const traverse = (node) => {

    arr.push(node.value);

    if(node.left) traverse(node.left);

    if(node.right) traverse(node.right);

  };

  traverse(tree1.root);

  let hashTable = new HashTable(arr.length);

  for(let value in arr){

    hashTable.set(value,value);

  }

  let results = [];

  const inHashTable = (node) => {

    if(hashTable.has(node.value) ) results.push(node.value);

    if(node.left) inHashTable(node.left);

    if(node.right) inHashTable(node.right);

  };

  inHashTable(tree2.root);

  return results;

}

