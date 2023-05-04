# The Merge Sort Method, a Blog

Merge Sort uses two methods to take an input numerical list and return a sorted version of that numerical list in ascending order.

Below is an example of pseudocode describing these methods:

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

The testable code for this method can be found in the adjacent file labeled merge_sort.py.

Let's look at an example input list: [8,4,23,42,16,15].

The first call of our merge_sort function splits our list into two haves, a left and right: [8, 4, 23] and [42, 16, 15].

Merge_sort calls itself again recursively on left and splits that into two halves as well: [8] and [4, 23].

Merge_sort calls itself again on left ([8]) which returns a list with a single element of 8.
Merge_sort is then called recursively on right ([4, 23]) and splits that into two halves: [4] and [23].
Merge_sort is then called recursively on both these lists of single elements, and determines that they are sorted.

Our merge function is then called with the sorted left and right halves of our elements that were most recently sorted ([4] and [23]).
The merge function takes in our two single element lists as left and right, and the just split list of [4, 23]. The merge function merges these two halves into: [4, 23].

The merge function is then called with the sorted left half ([8]), the sorted right half ([4, 23]), and the previously split list of [8, 4, 23]. The result is the sorted left half of our original list of: [4, 8, 23].

We then work our way back to the right half of our initial list split ([42, 16, 15]) and perform the same actions.

We ultimately arrive at a sorted right half of: [15, 16, 42].

Our merge function is then called on our sorted left and right halves of: [4, 8, 23] and [15, 16, 42].

Merge evaluates that 4 is smaller than 15 and pushes 4 into the first index position of our original list.
Merge then evaluates that 8 is smaller than 15 and pushes 8 into the next index position of our original list.
Merge then evaluates that 23 is larger than 15 and pushes 15 into the next index position of our original list.
Merge then evaluates that 23 is larger than 16 and pushes 16 into the next index position of our original list.
Merge then evaluates that 23 is smaller than 42 and pushes 23 into the next index position of our original list.
Merge evaluates that there are no remaining elements in the left half and does not execute that loop. Merge evaluates that there is one remaining element in the right half ([42]) and assigns that value to the final index position of our original list.

Our final result is a sorted list of [4, 8, 15, 16, 23, 42].
