# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
# Example
#
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return None
    else:
        return [len([i for i in arr if i > 0]), sum(i for i in arr if i < 0)]


def count_positives_sum_negatives2(arr):
    if not arr:
        return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += x
    return [pos, neg]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, -1, -2]))
print(count_positives_sum_negatives2([1, 2, 3, 4, 5, -1, -2]))