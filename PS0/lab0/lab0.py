# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x**3


def factorial(x):
    if type(x) is not int or x < 0:
        raise Exception("factorial: input must not be negative")
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def count_pattern(pattern, lst):
    if len(pattern) < 1 or len(lst) < 1:
        return 0
    pattern_string = ''.join([str(x) for x in pattern])
    lst_string = ''.join([str(item) for item in lst])

    return lst_string.count(pattern_string)


# Problem 2.2: Expression depth

def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    max_depth = 1  # Picks up outer list/tuple holding expr
    for item in expr:
        curr_depth = 1 + depth(item)
        max_depth = max(max_depth, curr_depth)
    return max_depth


# Problem 2.3: Tree indexing


def tree_ref(tree, index):
    raise NotImplementedError


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = "Working on it now"

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = "Not sure yet"

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = "Getting there"

# How many hours did this lab take?
HOURS = "2"


def main():
    '''
    Tests to check work
    '''
    test_depth = False

    if test_depth:
        depth_tests = [
            ['x', 0],
            [('expt', 'x', 2), 1],
            [('+', ('expt', 'x', 2), ('expt', 'y', 2)), 2],
            [('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1),
                                      ('/', 5, 2))), 4]
        ]

        for t in depth_tests:
            print "Testing", t[0], "should get", t[1]
            res = depth(t[0])
            if(res == t[1]):
                print "PASSED"
            else:
                print "FAILED - returned", res

    return 0


if __name__ == '__main__':
    main()
