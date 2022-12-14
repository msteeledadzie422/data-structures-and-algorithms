'use strict';

class Node {

  constructor(value) {

    this.value = value;

    this.next = null;

  }

}

class Queue {

  constructor(){

    this.front = null;

    this.rear = null;

  }

  enqueue(value){

    const node = new Node(value);

    if(this.front === null){

      this.front = node;

      this.rear = node;

    }else{

      this.rear.next = node;

      this.rear = node;

    }

  }

  dequeue(pref){

    if(this.front === null){return 'exception';}

    let finder;

    let previous = this.front;

    if(this.front.pref === pref){

      finder = this.front.value

      this.front = this.front.next;

      return finder;

    }

    let current = this.front.next;

    while(current !== null){

      if(pref === current.value.pref){

        finder = current.value.pref;

        previous = current.next;

        break;

      }

      previous = current;

      current = current.next;

    }

    return finder;

  }

}
