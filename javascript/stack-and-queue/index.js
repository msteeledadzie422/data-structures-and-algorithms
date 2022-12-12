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

class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
  }

  enqueue(value) {
    let result = new Node(value);
    let current = this.rear;

    if(current) {
      current.next = result;
    }

    this.rear = result;

    if(!this.front) {
      this.front = result;
    }
  }

  dequeue() {
    if(this.isEmpty()) {
      return 'Empty Queue';
    }

    let result = this.front;
    this.front = result.next;

    if(this.rear === result) {
      this.rear = result.next;
    }
  }

  peek() {
    if(this.isEmpty()) {
      return 'Empty Queue';
    }
    this.front.value;
    return this.front.value;
  }

  isEmpty() {
    let current = this.front;
    if(!current) {
      return true;
    }
    else {
      return false;
    }
  }
}

module.exports = { Node, Stack, Queue };
