"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place"""


def retrieve_natural_positives(l):
    return list(filter(lambda x: x > 0))


def first_missing(l):
    pass


assert first_missing([3, 4, -1, 1]) == 2
assert first_missing([1, 2, 0]) == 3
assert first_missing([-1, -2, -1]) == 1
assert not(first_missing([1, 2, 3]) == 3)  # negative test
