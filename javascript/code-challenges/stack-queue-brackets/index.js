'use strict';

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
  }

  push(value) {
    let top = this.top;
    let result = new Node(value);
    result.next = top;
    this.top = result;

  }

  pop() {
    let temp = this.top;
    if(this.isEmpty()) {
      return 'Empty';
    }
    this.top = temp.next;
    return temp.value;
  }

  peek() {
    let top = this.top;
    if(this.isEmpty()) {
      return 'Empty';
    }
    return top.value;
  }

  isEmpty() {
    let top = this.top;
    if(!top) {
      return true;
    }
    else {
      return false;
    }
  }
}

function validateBrackets(str) {
  let stack = new Stack;

  for(i = 0; i < str.length; i++) {
    let x = str[i];

    if (x === '(' || x === '{' || x === '[') {
      stack.push(x);
    } else if ((stack.top === '(' && x ===')') || (stack.top === '{' && x ==='}') || (stack.top === '[' && x ===']')) {
      stack.pop();
    } else return false;
  }
  return stack.length ? false : true;
}

validateBrackets('()[]{}');
