# removing all vowels in a string

def remove_vowels(s):
    for vowel in 'aeiou':
        s = s.replace(vowel, '')
    return s


def replace_vowels(s):
    s = s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    return s


print(remove_vowels('yo'))
print(replace_vowels('yo'))
