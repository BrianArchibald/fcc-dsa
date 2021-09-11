Here's a systematic strategy we'll apply for solving problems:

State the problem clearly. Identify the input & output formats.
Come up with some example inputs & outputs. Try to cover all edge cases.
Come up with a correct solution for the problem. State it in plain English.
Implement the solution and test it using example inputs. Fix bugs, if any.
Analyze the algorithm's complexity and identify inefficiencies, if any.
Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"Applying the right technique" is where the knowledge of common data structures and algorithms comes in handy.

## Problem 1 Linear Search , Sorted array that is rotated, how many times is it rotated.

##  Have sorted list that is rotated n times. Return n. There are no duplicates in the list

##  input :  [2,3,4,1]

##  answer : 1

## Other possible inputs : A list of size 10 rotated 3 times.
# A list of size 8 rotated 5 times.
# A list that wasn't rotated at all.
# A list that was rotated just once.
# A list that was rotated n-1 times, where n is the size of the list.
# A list that was rotated n times (do you get back the original list here?)
# An empty list.
# A list containing just one element.

## Test cases
test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}