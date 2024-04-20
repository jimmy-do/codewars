# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
# in descending order. Essentially, rearrange the digits to create the highest possible number. Examples:
#
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


def descending_order2(num):
    s = str(num)
    s = list(s)
    s.sort()
    s = reversed(s)
    s = ''.join(s)
    return int(s)


print(descending_order(3289450913))
print(descending_order2(3289450913))
