# Dict operations


a_dict = {'first_name': 'Minor', 'names_count': 2}


# Accessing a dict
print 'Complete dict:', a_dict
print 'Length of the dict:', len(a_dict)
print 'Value for key first_name:', a_dict['first_name']
print 'Value for key names_count:', a_dict['names_count']
print 'Keys:', a_dict.keys() # List; no guaranteed order
print 'Values:', a_dict.values() # List; no guaranteed ord
print 'Keys and value items:', a_dict.items() # List of tuples; no guaranteed order
print


# Modifying a dict
print 'dict before modification:', a_dict
del a_dict['first_name'] # Delete the mapping from 'first_name': 'Minor'
print 'dict after deleting first_name:', a_dict
a_dict['key3'] = True # Add a new mapping
print 'dict with key3 added:', a_dict


# Useful idiom
a_dict.setdefault('key4', 4) # Set key4 to 4 iff it does not contain a key4 already