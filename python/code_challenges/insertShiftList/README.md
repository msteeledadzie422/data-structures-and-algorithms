# Lists

Insert and shift an array in middle at index.

## Challenge

Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard

![Whiteboard](./insertShiftList.png)

## Approach & Efficiency

We initialize a new list with our given value. We then find the midpoint of our given list.

We use a for loop to loop through the list, adding numbers to the left and right of the given value in our new array until the midpoint itself is reached, breaking the loop.

## Partner

Ethan Albers
