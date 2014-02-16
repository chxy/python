# All loops can be expressed as while <condition>: block
# But we have special syntax for some common forms of loops.

a_list = [1, 2, True]

# Task: print each element of the list on a separate line

# The clunky while form:
print 'While'
i = 0
while i < len(a_list): # len(a_list) = length of the list, in this case 3
    print a_list[i]
    i += 1
print

# The nicer for loop:
print 'For'
for element in a_list: # Spoken as "for each element in a_list"
    print element
print


# Unlike other languages, Python has no "indexed for". Every for loop is "for-each".
# If you want to loop over numbers:
print 'For over numbers'
for i in xrange(10): # for each i in [0, 10)
    print i
print
# xrange is flexible:

print 'For over numbers'
for i in xrange(1, 10, 2): # for each i in [1, 10) stepping 2 each iteration
    print i
print

