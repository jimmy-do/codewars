# Take an array and remove every second element from the array. Always keep the first element and start removing with
# the next element. Example:
#
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!


def slicing_remove_elements(arr):
    return arr[::2]


print(slicing_remove_elements(['yo', 'ayo', 'me', 'I', 'you']))
