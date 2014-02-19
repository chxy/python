# A string is a sequence of characters
string_variable = "String"
string_variable = 'String' # Same as above

# An integer (aka int) can be -2**31 to 2**31-1 i.e., 32 bits
integer_variable = 0

# Long integers (aka long) are all other integers
long_variable = 2147483648L # 2*31

# Bonus question: why two integer types?
# Performance reasons: 32-bit processors can do arithmetic on 32-bit values much quicker than larger or smaller values.

boolean_variable = True
boolean_variable = False

# A list is a mutable (changeable) sequence of elements
# Elements can have different (mixed) types
list_variable = [1, 2, True]

# Mutable types are where "variable is a name" comes into play:
list_original = [1, 2]
list_alias = list_original
del list_original[1] # Remove the second element (0-based indices!) of list_original
# list_original is now [1]
# What is list_alias? [1, 2] or [1]?

# A tuple is an immutable (unchangeable) sequence of elements
# Elements can have different types
tuple_variable = (1, 2, True)
tuple_variable_with_one_element = (1,)
# Can't do this: del tuple_variable[1]

# Bonus question: why have two sequence types, one mutable (the list) and one immutable (the tuple)?

# A dictionary (aka dict) maps unique keys to any values
dict_variable_with_string_keys_and_values = {'first_name': 'Minor', 'last_name': 'Gordon'}
dict_variable_with_string_keys_and_integer_values = {'key1': 1, 'key2': 1}
dict_variable_with_integer_keys_and_string_values = {1: 'value1', 2: 'value2'}
dict_variable_with_mixed_types = {'key1': 1, 2: 'value2'} # Mutable, mixed types

# None (called null in some languages) indicates the absence of a value
none_variable = None

# Get the type of a variable
print type(tuple_variable)