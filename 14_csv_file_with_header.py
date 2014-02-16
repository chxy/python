import csv

with open('regents.csv') as f:
    # Loop over the rows again, but using enumerate(sequence) to give us the row number as well
    for row_i, row in enumerate(csv.reader(f)):
        print 'Row number', row_i

        if row_i == 0:
            headers = row
            continue

        values = row

        # Loop over each column
        for column_i in range(len(headers)):
            header = headers[column_i]
            value = values[column_i]
            print header, ':', value
        print

        # Better way: zip loops over two sequences at once
        for header, value in zip(headers, values):
            print header, ':', value

        print
        print
