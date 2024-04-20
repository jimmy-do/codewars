# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element - by value,
# not by index!
#
# The highest or lowest element respectively is a single element at each edge, even if there are more than one with
# the same value.
#
# Input validation:
#
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or
# a list with only 1 element, return 0.

def excluding_highest_lowest(arr):
    return sum(sorted(arr)[1:-1]) if len(arr) and arr > 0 else 0


print(excluding_highest_lowest([1, 2, 3, 4, 5]))
print(excluding_highest_lowest([]))
