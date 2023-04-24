# The InsertionSort Method, a Blog

InsertionSort uses two methods to take an input numerical list and return a sorted version of that numerical list in ascending order.

Below is an example of pseudocode describing these methods:

Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

The testable code for this method can be found in the adjacent file labeled insertion_sort.py.

Let's look at an example input list: [8,4,23,42,16,15].

Our InsertionSort method first takes in our input list and creates a new array called sorted with the value of the input list's zero index position set as the value of the zero index position of this new list called sorted.

Right now, sorted would look like this: sorted = [8]

From there we use a for loop in our InsertionSort method (starting at index position 1, not 0) to run our Insert method on each remaining value in the input list, checking that value against what is in the sorted list. Ultimately, we will be returning the new list we will be generating called sorted.

The first pass of our methods evaluates the 1 index position of our input list (4) against our sorted list [8].

Because 4 is smaller than 8 at sorted's current index position 0, we store 8 in a temp variable, and set sorted's new 0 index position to 4, the current index 1 position of the input list, which was stored in our value variable.

Our method then set's our value variable to our temp variable (8), and appends value to our sorted list, which now looks like this: sorted = [4,8].

The second pass of our methods evaluates the 2 index position of our input list (23) against our sorted list [4,8].

As our value variable of 23 is greater than all current values within sorted, we simply append 23 to the end of sorted, which now looks like this: [4,8,23].

The third pass of our methods evaluates the 3 index position of our input list (42) against our sorted list [4,8,23].

As our value variable of 42 is greater than all current values within sorted, we simply append 23 to the end of sorted, which now looks like this: [4,8,23,42].

The third pass of our methods evaluates the 4 index position of our input list (16) against our sorted list [4,8,23,42].

Our Insert method finds that our value variable of 16 is smaller than 23 at sorted's index position 2 and sets 16 as sorted's new value at index position 2, storing 23 in our temp variable. Our temp variable would then be swapped with our value variable, i would be incremented (because i is still less than sorted.length), and 23 would be appended to the end of sorted.

Our value variable would now be 23, and our while loops would run again, comparing our new value variable of 23 to the next sorted's next (and now final) index position of 3, which has a value of 42.

Our Insert method would find that our value variable of 23 is smaller than 42 at sorted's index position 3, and would set 23 as sorted's new value at index position 3, storing 42 in our temp variable. Our temp variable would then be swapped with our value variable, and 42 would be appended to sorted, as i is now equal to sorted.length. Sorted would now look like this: sorted = [4,8,16,23,42].

The fourth pass of our methods evaluates the 5 index position of our input list (15) against our sorted list [4,8,16,23,42].

Similar to the previous pass, our Insert method finds that our value variable of 15 is smaller than 16 at sorted's index position 2 and sets 15 as sorted's new value at index position 2, storing 16 in our temp variable.

Also similar to our previous steps, our Insert method would evaluate our new value variable of 16 against our sorted lists's values, and swap it with sorted's 23, then in turn would swap that 23 with sorted's 42, and would ultimately "append" 42 to the end of sorted.

Having iterated through the final element of our input list, our sorted list would now look like this: sorted = [4,8,15,16,23,42].

Our InsertionSort method would then return our sorted list.
