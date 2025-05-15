'''

WHAT IS A HASH MAP?

 A hash map is a data structure
 It allows you to store pairs and get values based on the keys.
 Used usually when you need access to data quickly

'''

# Step 1.) Create the Hash Map | For Python --> Initialize a hash map using curly braces to enclose key-value pairs
hash_map = {}

# Step 2.) Add key-value pairs to the hash map --> 
hash_map['('] = ')'
hash_map['['] = ']'
hash_map['{'] = '}'

# '(', '[', '{' are the keys of the hash map.
# '}', ']', ')' are the values of the hash map

# Step 3.) Retrieve the values from the hash map
print(hash_map['(']) # Will output: ')'
print(hash_map['[']) # Will output: ']' 
print(hash_map['{']) # Will output: '}'
