# Multi-Bracket Validation

*Feature Tasks*
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Whiteboard Process
![Whiteboard](./stack_queue_brackets.png)

## Approach & Efficiency
For this we set the fizz buzz division parameters within the first portion of our method to generate the new node values for our new kary tree.

From there we recursively call the function on each of the nodes children to generate new children for that node, and all subsequent nodes.

Once the new kary tree is created, it is necessary to traverse this new tree to see that all values have been converted correctly.

## Solution
This code can be run using the command 'python3 code_challenges/stack_queue_brackets/stack_queue_brackets.py' and tested using the command 'pytest code_challenges/stack_queue_brackets'.
