def show_magicians(magicians):
    """"Print all the magicians names"""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Append 'the Great' to magicians by returning a new list"""
    theGreatMagicians = []
    for magician in magicians:
        theGreat = "the Great " + magician
        theGreatMagicians.append(theGreat)
    magicians_names = theGreatMagicians
    return magicians_names

magicians_names = ['dumbledore', 'some guy', 'dumbledore is not a magician']

magicians_names2 = make_great(magicians_names[:])   # due to the logic of the code this exercise is almost pointless
show_magicians(magicians_names)
show_magicians(magicians_names2)
