import sys

# Expect at least one score from command line arguments
if len(sys.argv) < 2:
    print("Usage: python array_scores.py <score1> <score2> <score3> ...")
    sys.exit()

# Convert command line arguments to a list of integers
scores = list(map(int, sys.argv[1:]))

# Calculate sum, average, maximum and minimum
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
