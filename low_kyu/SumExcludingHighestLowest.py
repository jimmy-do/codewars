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

def exclude_highest_lowest(listy):
    return sum(sorted(listy)[1:-1]) if sum(listy) and len(listy) > 0 else 0


print(exclude_highest_lowest([1, 2, 3, 4, 5]))
print(exclude_highest_lowest([0, 0]))
