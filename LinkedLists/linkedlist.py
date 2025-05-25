'''
What is a Linked List?

It's a type of data structure. 
Each element known as a node has a value.
It also has a reference known as a pointer to the next node.

Usually used when you need to quickly add and/or delete something (especially at the start or in the middle)

A Singly Linked List....

A linked list that goes in one direction only.
Each of its nodes point to the next node only.

'''

# Step 1.) Define a class for nodes
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # This is the value for the node you are currently on
        self.next = next    # This is the pointer to the next node... If there is no next, then it points to none

# Step 2.) Manually creating the nodes. 
# Referencing the problem I was solving on LeetCode "Add Two Numbers" -->
# The linked lists stores the numbers in the nodes backwards. So if I want to store 123 in a linked list, I need store it: 3 -> 2 -> 1
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)

# Now connect the nodes or make the nodes point to the next one like explained above ^
node1.next = node2  # 3 -> 2
node2.next = node3  # 2 -> 1

# Node 1 would now be the head of the list: 3 -> 2 -> 1

# Step 3.) Write a function to go through the linked list and then print the values of the nodes
def print_nodes(head):
    while head:
        print(head.val, end=' -> ')

        head = head.next

    print("None")

# print_nodes(node1)

# Step 4.) Dynamic approach
practice_list = [3, 2, 1] # backwards just like the leetcode problem
dummy_node = ListNode()
current_node_pointer = dummy_node

for val in practice_list:
    current_node_pointer.next = ListNode(val)

    current_node_pointer = current_node_pointer.next

print_nodes(dummy_node.next)

    

