'''
WHAT IS A STACK?

A stack is another type of data structure that follow the Last In, First Out concept (LIFO)

Compare it to a stack of plates where -->

Adding a plate to the top is a --> PUSH
Removing a plate from the top is a --> POP
The only place where you can access a plate is from the top --> cant access a plate that's in the middle or the bottom

PURPOSE OF A STACK?

Good for when you need to reverse something, track nested stuff, or undo any operations.

The LeetCode Valid Parenthese problem, a stack will help match the brackets correctly because the last open bracket should be the first one to close

'''

# Stack Code

# Using a -- LIST -- as a STACK
stack = []

# Push items onto the stack
stack.append('a') # Stack will now be ['a']
stack.append('b') # Stack will now be ['a', 'b']
stack.append('c') # Stack will now be ['a', 'b', 'c' ]

# Pop items from the stack
item = stack.pop() # Removes and returns 'c', stack will now be ['a', 'b']
print(item) # Outputs the item that got popped --> In this case, it's c | Outpuut: 'c'
