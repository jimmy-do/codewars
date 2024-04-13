geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds = ['African', 'Vietnamese', 'Indonesian']


def goose_filter(birdies):
    for b in birdies:
        if b in geese:
            birds.remove(b)
    return birds


print(goose_filter(birds))
