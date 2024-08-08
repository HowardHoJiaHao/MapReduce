# Mapper code Total Word Count

#!/usr/bin/env python
import sys
import csv

# Create a CSV reader that reads from standard input
reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')

# Skip the header row (if there is one)
next(reader, None)

# Process each row
for row in reader:
    try:
        # Check if the row has at least 10 columns
        if len(row) < 10:
            continue

        # Assuming the 10th column is the text column
        text = row[9]

        # Split the text into words
        words = text.split()
        
        # Output each word with a count of 1
        for word in words:
            print(f'{word}\t1')
    except csv.Error as e:
        # Handle CSV parsing errors
        sys.stderr.write(f"CSV error: {e}\n")
    except Exception as e:
        # Handle other unexpected errors
        sys.stderr.write(f"Unexpected error: {e}\n")