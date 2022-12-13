'use strict';

class PseudoQueue {
  constructor () {
    this.enqueueStack = [ ];
    this.dequeueStack = [ ];
  }

  push(value) {
    this.enqueueStack.push(value);
  }

  pop() {
    if (!this.enqueueStack.length) {
      while(this.enqueueStack.length) {
        this.dequeueStack.push(this.enqueueStack.pop());
      }
    }
    return this.dequeueStack.pop();
  }
}
