# Reducer code Total Word Count

#!/usr/bin/env python
import sys

total_word_count = 0

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

            # Update the total word count
            total_word_count += count
    except Exception as e:
        # Handle unexpected errors
        sys.stderr.write(f"Unexpected error: {e}\n")

# Output the total word count
print(f'Total Word Count\t{total_word_count}')