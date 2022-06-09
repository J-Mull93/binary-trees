# Input: A string of text
# Output: The string with spaces removed, newline characters removed
def preprocess_text(txt):
    # Remove new line & spaces
    txt = txt.replace("\n", "")
    txt = txt.replace(" ", "")

    # Remove obsolete empty children from leaf nodes
    txt = txt.replace("()()", "")
    return txt


# Function to identify the next integer in a tree
# Input: A string whose first character is an integer
# Output: The first who integer in the string as an integer
# Note - this may be multiple characters long in the string
def identify_integer(txt):
    n = ""
    ix = 0
    # Concatenate the digit characters as a string until first non-digit
    while txt[ix] not in ("(", ")"):
        n += txt[ix]
        ix += 1
    # Return the integer as an integer
    return int(n)


# Function to identify the next tree in a file
# Input: A string whose first character is '(' to start a tree
# Output: A string corresponding to the entire first tree in the string
def identify_tree(txt):
    # Initiate a tree with known first character
    tree = "("
    # Variable to hold depth of tree - terminate when it reaches 0 (tree complete)
    depth = 1
    ix = 1
    # Add characters to the new tree string
    while depth != 0:
        tree += txt[ix]
        # Update the depth - going to a child if '(' (-1), or up to parent if ')' (+1)
        if txt[ix] == ")":
            depth -= 1
        elif txt[ix] == "(":
            depth += 1
        ix += 1
    # Return the tree as a string
    return tree


# Function to record integer-tree pairs in a dataframe
# Input: A dataframe with 2 columns and a string containing integer-tree pairs
# Output: The dataframe with one row for each integer-tree pair
def record_pairs(txt, df):
    while len(txt) > 0:
        # Identify the next integer and remove it from the string
        n = identify_integer(txt)
        txt = txt[len(str(n)):]

        # Identify the next tree and remove it from the string
        tree = identify_tree(txt)
        txt = txt[len(tree):]

        # Add the integer-tree pair to the dataframe
        df.loc[len(df)] = [n, tree]
    return df


# Function to record all root-leaf path sums in a tree
# Input: A string corresponding to a tree
# Output: A list of all root-leaf path sums of node values
def calc_path_sums(tree):
    # Check if the tree is empty and return None if so
    if tree == "()":
        return None
    # If not empty remove obsolete empty children nodes
    # All and only leaf nodes are now followed by ")"
    else:
        tree = tree.replace("()", "")

    # Initialise variable to hold the root-leaf path sum value and current path traversed by algorithm
    path_values = []
    current_path = []
    ix = 0
    # Iterate through the string in the tree
    while ix < (len(tree) - 1):

        if tree[ix] == "(":
            # If at a right bracket find next integer
            # Allow index to skip past the integer
            # Add integer to path traversed
            n = identify_integer(tree[ix + 1:])
            ix += (1 + len(str(n)))
            current_path += [n]

        elif tree[ix - 1] != ")":
            # If at left bracket and previous character wasn't the last integer was a leaf
            # Add current path sum to path_values
            # Then increment index and remove the leaf node from the current path
            path_values += [sum(current_path)]
            ix += 1
            current_path = current_path[:-1]

        else:
            # If at left bracket and previous character was then we move to a parent from a non-leaf
            # Remove the end node from the current path
            ix += 1
            current_path = current_path[:-1]
    return path_values


# Function to identify if an integer is the sum of a root-leaf path in a tree
# Input: An integer and a string corresponding to a tree
# Output: Boolean True or False value
def integer_path_check(n, tree):
    return n in calc_path_sums(tree)


# Function to create file of results for integers are the sum of a root-leaf path in a paired tree
# Input: A dataframe containing integer-tree pairs and a filename
# Output: A file containing one result per line
# 'yes' if some root-leaf path in the tree sums to the integer
# 'no' otherwise
def output_results(df, filename):
    # Create and open the file with the given filename
    f = open(filename, "w")

    # Loop through the integer-tree pairs and record the results
    for ix in range(len(df.index)):
        n = df.iat[ix, 0]
        tree = df.iat[ix, 1]
        # Record the result appropriately
        # Use of \n ensures each result is on a new line
        if integer_path_check(n, tree):
            f.write("yes\n")
        else:
            f.write("no\n")

    f.close()
