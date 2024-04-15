import string


# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return
# the resulting string.
#
# Note: input will never be an empty string
def fake_binary(num):
    return ''.join('0' if v < '5' else '1' for v in num)


def newnew(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))


print(fake_binary('12345'))
print(newnew('GATTACA'))
print(str.maketrans('1', '2'))