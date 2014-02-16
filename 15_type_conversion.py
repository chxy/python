import csv

with open('regents.csv') as f:
    for row_i, row in enumerate(csv.reader(f)):
        if row_i == 0:
            headers = row
            continue

        values = row

        for header, value in zip(headers, values):
            if header == 'Headcount':
                headcount = value
                if headcount == 348:
                    print 'This row must be Fall 2013 / UNI / Graduate / Non-Resident'
                else:
                    print row
                    print "That's never going to work, since type(headcount)=", type(headcount), "and type(348)=", type(348)

                # Convert headcount from a str to an int
                headcount_int = int(headcount)
                if headcount_int == 348:
                    print 'This row must be Fall 2013 / UNI / Graduate / Non-Resident:', row


# Other common conversions
x = 10 # Int
x_str = str(x) # To str
if x_str == '10':
    print 'Equal now'

t = [1, 2, True] # List
t_tuple = tuple(t) # To tuple
t_list = list(t) # Back to list

b = '' # Str
b_bool = bool(b) # To boolean
print 'Bool conversion', b_bool
# Python has some odd rules for converting values to bool. Just be wary of this.
