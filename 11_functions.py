def add(x, y):
    # Add the contents of two variables x and y
    # Note the indentation: that tells Python what's in the function (its "block") and what's outside it
    return x + y
# No longer in the function

z = add(1, 2) # Call the function and store its result in the variable z
print z

# Functions allow for code reuse ("Don't Repeat Yourself")

def change_list(a_list):
    del a_list[0]
    a_list.append('test')
some_list = ['a', 'b']
change_list(some_list) # some_list "becomes" a_list in change_list
some_other_list = ['b', 'c']
change_list(some_other_list) # some_other_list "becomes" some_other_list in change_list
