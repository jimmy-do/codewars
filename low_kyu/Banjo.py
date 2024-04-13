# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:

def are_you_playing_banjo(name):
    name = name.lower()
    if name[0] == 'r':
        return True
    else:
        return False


print(are_you_playing_banjo('Rimmy'))
