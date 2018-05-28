import random
def points(n):
    directory = {}
    for i in range(0, n):
        pname = chr(ord('a') + i)
        x = 1000.0 * random.random()
        y = 1000.0 * random.random()
        directory[pname] = (x, y)
    print(directory)
    return directory


points(5)
