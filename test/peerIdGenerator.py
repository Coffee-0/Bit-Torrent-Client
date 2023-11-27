import random


def generator():
    return "-PC0001-" + "".join([str(random.randint(0, 9)) for _ in range(12)])


peerID = generator()
print(peerID)
