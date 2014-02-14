import csv # Import the csv library

with open('regents.csv') as f:
    # File block again

    # Loop over each row in the CSV
    for row in csv.reader(f):
        print row
