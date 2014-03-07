# Library imports. Don't worry about the mechanics of this yet.
import csv # CSV reading
import os.path # File system manipulation
import pprint # Pretty printer


csv_file_path = "C:\\Users\\minor\\projects\\personal\\python\\regents.csv"


# Build the tree: beginner
beginner_tree = {}
with open(csv_file_path) as csv_file:
    row_i = 0
    for row in csv.reader(csv_file):
        if row_i == 0:
            pass # Don't care about headers
        else:
            values = row
            semester = values[0]
            uni = values[1]
            student_class = values[2]
            resident_status = values[3]
            headcount = int(values[4]) # Convert from string to integer

            if semester in beginner_tree:
                unis = beginner_tree[semester]
            else:
                unis = {}
                beginner_tree[semester] = unis

            if uni in unis:
                student_classes = unis[uni]
            else:
                student_classes = {}
                unis[uni] = student_classes

            if student_class in student_classes:
                resident_statuses = student_classes[student_class]
            else:
                resident_statuses = {}
                student_classes[student_class] = resident_statuses

            resident_statuses[resident_status] = headcount

        row_i = row_i + 1
        # Now back to the top of the for loop


# Build the tree: intermediate without headers
intermediate_tree = {}
with open(csv_file_path) as csv_file:
    for row_i, row in enumerate(csv.reader(csv_file)):
        if row_i == 0:
            continue # To the top of the for loop, since we don't really care about headers here

        # Most of the code we care about is in the "else" branch where row_i > 0,
        # so just use continue to skip the rest of the for loop body so we don't have to
        # indent again.

        values = row
        semester = values[0]
        uni = values[1]
        student_class = values[2]
        resident_status = values[3]
        headcount = int(values[4])

        intermediate_tree.setdefault(semester, {}).setdefault(uni, {}).setdefault(student_class, {})[resident_status] = headcount


# Build the tree: intermediate with headers
intermediate_tree_2 = {}
with open(csv_file_path) as csv_file:
    for row_i, row in enumerate(csv.reader(csv_file)):
        if row_i == 0:
            headers = row
            continue

        values = row
        values_dict = {}
        for header, value in zip(headers, values): # Iterate over two sequences at once
            values_dict[header] = value

        # Can use \'s to spread a single language line (i.e., a statement) over multiple lines of text
        # It's the same meaning as having everything on the same line, just prettier.
        intermediate_tree_2\
            .setdefault(values_dict['Year'], {})\
            .setdefault(values_dict['University Name'], {})\
            .setdefault(values_dict['Student Classification'], {})\
                [values_dict['Resident Status']] = int(values_dict['Headcount'])


# Build the tree: advanced
advanced_tree = {}
with open(csv_file_path) as csv_file:
    for row_i, row in enumerate(csv.reader(csv_file)):
        if row_i == 0:
            continue
        branch = advanced_tree
        for column in row[:-2]:
            branch = branch.setdefault(column, {})
        branch[row[-2]] = int(row[-1])


# All of the ways we built the tree should have the same result
# Use assert <condition> to assert that
# If the condition is false this will stop the program with an error
assert beginner_tree == intermediate_tree == intermediate_tree_2 == advanced_tree


# Iterate over the tree and pretty-print it with indentation
for year in beginner_tree.keys():
    print year
    for uni in beginner_tree[year].keys():
        print '  ', uni
        for student_class in beginner_tree[year][uni].keys():
            print '    ', student_class
            for resident_status in beginner_tree[year][uni][student_class].keys():
                print '      ', resident_status
                headcount = beginner_tree[year][uni][student_class][resident_status]
                print '        ', headcount
print # Empty line

# Simpler: use .items() instead of .keys() to iterate over (key, value) tuples together
for year, unis in beginner_tree.items():
    print year
    for uni, student_classes in unis.items():
        print ' ' * 2, uni # ' ' * 2 = repeat the string ' ' two times
        for student_class, resident_statuses in student_classes.items():
            print ' ' * 4, student_class
            for resident_status, headcount in resident_statuses.items():
                print ' ' * 6, resident_status
                print ' ' * 8, headcount
print

# Or just use this nice library function:
pprint.pprint(beginner_tree)
print


# Traverse the tree looking for something, in this case the number of students classed "Graduate"
grad_students = 0
for year, unis in beginner_tree.items():
    for uni, student_classes in unis.items():
        for student_class, resident_statuses in student_classes.items():
            for resident_status, headcount in resident_statuses.items():
                if student_class == 'Graduate':
                    grad_students += headcount
print 'Total number of graduate students', grad_students
print


# We could also get a simple sum from the original data, of course
grad_students_confirmation = 0
with open(csv_file_path) as csv_file:
    for row_i, row in enumerate(csv.reader(csv_file)):
        if row_i == 0:
            continue # Skip the headers row
        values = row
        student_class = values[2]
        headcount = int(values[-1])
        if student_class == 'Graduate':
            grad_students_confirmation += headcount
assert grad_students == grad_students_confirmation


# As an aside, with "messy" data input by users you'll often want to change cases of strings because everything in Python is case-sensitive
# For example, if people could enter different cases for "Graduate" i.e. "graduate", "Graduate", "GRADUATE", et al., you'd want to say
#   if student_class.lower() == 'graduate'
# If you had hyphens as well you might want:
#   if student_class.replace('-', '').lower() == 'postdoctoral'
# Meaning, "take the string student class, replace all hyphens ('-') with an empty string ('') = remove all hyphens,
#   then take the result of that and convert it to lower case."
# If you might have whitespace on either side:
#   if student_class.strip().lower() == 'graduate'
# And so on. See http://docs.python.org/2/library/stdtypes.html#string-methods for more on string manipulation.

