# Mapper code Top 10 Words

#!/usr/bin/env python
import sys
import csv
import re

# List of stop words to filter out
stop_words = set([
    'the', 'a', 'an', 'in', 'on', 'and', 'is', 'of', 'to', 'for',
    'with', 'at', 'by', 'from', 'that', 'this', 'it', 'as', 'be',
    'are' ,'i' ,'you','will', 'we','has', 'have', 'not'
])

# Create a CSV reader that reads from standard input
reader = csv.reader(sys.stdin, delimiter=',', quotechar='"')

# Skip the header row (if there is one)
next(reader, None)

# Regular expression to remove symbols and punctuation
pattern = re.compile(r'[^a-zA-Z0-9\s]')

# Process each row
for row in reader:
    try:
        # Check if the row has at least 10 columns
        if len(row) < 10:
            continue

        # Assuming the 10th column is the text column
        text = row[9]
        
        # Remove symbols and punctuation
        text = pattern.sub('', text)

        # Split the text into words
        words = text.split()

        # Output each word with a count of 1 if it's not a stop word
        for word in words:
            word = word.lower()  # Convert to lowercase
            if word not in stop_words:
                print(f'{word}\t1')
    except csv.Error as e:
        # Handle CSV parsing errors
        sys.stderr.write(f"CSV error: {e}\n")
    except Exception as e:
        # Handle other unexpected errors
        sys.stderr.write(f"Unexpected error: {e}\n")
