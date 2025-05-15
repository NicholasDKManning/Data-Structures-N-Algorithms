# Hash Maps (Python)

A **hash map** (also known as a dictionary in Python) is a powerful data structure used to store **key-value pairs**. It allows for **fast lookup, insertion, and deletion** — typically in constant time, O(1).

This simple example in Python demonstrates how to create a hash map, add pairs, and retrieve values — a foundational concept used in countless coding interview problems.

---

## What's a Hash Map?

- A data structure that stores data in key-value pairs.
- Uses a **hash function** to compute an index (slot) in an underlying array.
- Ideal for situations where quick data retrieval by key is needed.

---

## 💻 Example Code (Python)

```python

# Step 1: Create an empty hash map
hash_map = {}

# Step 2: Add key-value pairs to the hash map
hash_map['('] = ')'
hash_map['['] = ']'
hash_map['{'] = '}'

# Step 3: Retrieve values from the hash map
print(hash_map['('])  # Output: ')'
print(hash_map['['])  # Output: ']'
print(hash_map['{'])  # Output: '}'
