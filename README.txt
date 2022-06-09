Problem:
Given a binary tree of integers we wish to knowwhether there exists a root-to-leaf
path whose nodes sum to a specified integer. 

Binary trees are represented as LISP S-expressions having the following form:

Kind of Tree	Representation in File

general tree	(integer tree tree)
empty tree		()


Example:
The tree below has four root-to-leaf paths whose sums are 27, 22, 26, and 18.
(5 (4 (11 (7 () ()) (2 () ()) ) ()) (8 (13 () ()) (4 () (1 () ()) ) ) )


Solution / Files:
A set of functions used to solve the problem are defined in binary_trees.py
The problem is solved by the script in individual_challenge.py using pandas and binary_trees.py
Test cases are contained in test_cases.txt
Results from applying individual_challenge.py to test_cases.txt are stored in results.txt
Requiremnts (business & technical) & linked test cases are stored in documentation.xlsx
