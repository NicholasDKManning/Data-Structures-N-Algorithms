Singly Linked Lists (Python)
A linked list is a fundamental data structure where elements (called nodes) are connected in a sequence using pointers. Each node contains a value and a reference to the next node in the list.

This example demonstrates how to define a node class, manually build a list, traverse it, and dynamically construct a list from an input array — using a real-world coding interview problem (“Add Two Numbers”) as context.

📘 What's a Linked List?
A linked list stores data in nodes.

Each node has:

A value (the data)

A pointer to the next node.

It’s useful when you need to quickly insert or delete elements, especially at the start or in the middle of a collection.

Singly Linked List:
Moves in one direction.

Each node points only to the next node.

💻 Example Code (Python)
python
Copy
Edit
# Step 1: Define a class for nodes
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # Value of the node
        self.next = next      # Pointer to the next node

# Step 2: Manually create and link nodes (example: 3 -> 2 -> 1)
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(1)

node1.next = node2
node2.next = node3

# Step 3: Function to print the linked list
def print_nodes(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print("None")

# print_nodes(node1)  # Output: 3 -> 2 -> 1 -> None

# Step 4: Dynamically create a linked list from a list
practice_list = [3, 2, 1]  # Input list (reversed form of 123)
dummy_node = ListNode()
current = dummy_node

for val in practice_list:
    current.next = ListNode(val)
    current = current.next

print_nodes(dummy_node.next)  # Output: 3 -> 2 -> 1 -> None
