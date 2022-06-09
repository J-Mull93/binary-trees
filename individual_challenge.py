# Import modules used to solve the challenge
# binary_trees is a module I've created for this purpose
import pandas as pd
import binary_trees as bt

# Read in the test cases from a file called IntegerTreePairs.txt
with open('IntegerTreePairs.txt') as f:
    text = f.read()

# Remove spaces, new line characters
# Also removes ()() denoting the empty nodes after a leaf
# Single empty nodes are retained at this point (where a node has one valid child)
clean_text = bt.preprocess_text(text)

# Set up an empty dataframe to store integer-tree pairs
integer_tree_pairs = pd.DataFrame(columns=["Integer", "Tree"])

# Stores each integer-tree pair in a new row in the dataframe
integer_tree_pairs = bt.record_pairs(clean_text, integer_tree_pairs)

# Creates an output file with the results
# Each result is on a new line
# Returns 'yes;' if any root to leaf path sums to the integer
# # Returns 'no' otherwise
bt.output_results(integer_tree_pairs, 'results.txt')
