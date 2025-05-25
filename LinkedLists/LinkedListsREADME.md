Singly Linked Lists (Python)
A singly linked list is a type of data structure where each element (called a node) holds a value and a pointer to the next node. Unlike arrays, linked lists don't store items in contiguous memory — they rely on references.

They're ideal for situations where you need to quickly insert or delete elements, especially at the beginning or middle of a sequence.

This simple example in Python demonstrates how to define nodes, manually link them, and dynamically build a linked list from a list — a foundational concept often used in coding interview problems.

What's a Linked List?
A data structure made up of nodes.

Each node stores:

A value

A pointer to the next node

In a singly linked list, the list moves in only one direction.

Useful for efficient insertion and deletion without shifting elements like in arrays.

💻 Example Code (Python)
python
Copy
Edit
# Step 1: Define the node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # Value of the current node
        self.next = next      # Pointer to the next node

# Step 2: Manually create and connect nodes (e.g. 3 -> 2 -> 1)
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

# Step 4: Dynamically create a linked list from a Python list
practice_list = [3, 2, 1]  # Represents the number 123 reversed

dummy_node = ListNode()  # Temporary starter node
current = dummy_node

for val in practice_list:
    current.next = ListNode(val)
    current = current.next

print_nodes(dummy_node.next)  # Output: 3 -> 2 -> 1 -> None
