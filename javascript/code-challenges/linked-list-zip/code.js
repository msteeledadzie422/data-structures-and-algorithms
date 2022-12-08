'use strict';

function zipLists(list1, list2) {

  let p1 = list1.head;

  let p2 = list2.head;



  let result = new LinkedList();

  let count = 0;

  if(p1) {

    result.head = p1;

    p1 = p1.next;

    count++;

  } else if(p2) {

    result.head = p2;

    p2 = p2.next;

  } else {

    return result;

  }



  let current = result.head;



  while (p1 && p2) {

    if (count % 2 === 0) {

      current.next = p1;

      current = current.next;

      p1 = p1.next;

    } else {

      current.next = p2;

      current = current.next;

      p2 = p2.next;

    }

  }



  let rem = p1 ? p1 : p2;



  while (rem) {

    current.next = rem;

    current = current.next;

    rem = rem.next;

  }

  return result;

}
