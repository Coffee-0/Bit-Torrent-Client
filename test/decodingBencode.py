from bencode import encode, decode

# An integer value starts with an 'i' followed by a series of
# digits unitl terminated with an 'e'
value = decode(b"i123e")
print(value)

# a string value starts by defining the number of characters
# contained within the string, followed by an actual string.
# string returned is a binary string.
value = decode(b"12:Middle Earth")
print(value)

# a list starts with a 'l' followed by number of objects, until terminated
# with an 'e'
# a list may contain any type of object
value = decode(b"l4:spam4:eggs6:grapesi123ee")
print(value)

# A dict starts with a 'd' and is terminated with an 'e'.
# objects in between must be pairs of string + objects
value = decode(b"d3:cow3:moo4:spam4:eggse")
print(value)
