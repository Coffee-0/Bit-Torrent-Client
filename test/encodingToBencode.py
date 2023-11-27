from collections import OrderedDict
from bencode import encode

value = encode(123)
print(value)

value = encode("Middle Earth")
print(value)

value = encode(["spam", "eggs", 123])
print(value)

d = OrderedDict()
d["cow"] = "moo"
d["spam"] = "eggs"
value = encode(d)
print(value)
