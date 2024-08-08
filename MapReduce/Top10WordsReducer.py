# Reducer code Top 10 Words

#!/usr/bin/env python
import sys
from collections import defaultdict

# Dictionary to store the counts of each word
word_counts = defaultdict(int)

# Read input from standard input
for line in sys.stdin:
    try:
        # Remove leading and trailing whitespace
        line = line.strip()
        
        # Parse the input we got from the mapper
        if '\t' in line:
            word, count = line.split('\t', 1)
            
            # Convert count from string to int
            try:
                count = int(count)
            except ValueError:
                # Count was not a number, so silently ignore this line
                continue
            
            # Update the count for the word
            word_counts[word] += count
    except Exception as e:
        # Handle unexpected errors
        sys.stderr.write(f"Unexpected error: {e}\n")

# Get the top 10 words by count
top_10_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Output the top 10 words and their counts
for word, count in top_10_words:
    print(f'{word}\t{count}')