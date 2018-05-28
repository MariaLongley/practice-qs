def search(s, slst, size):
    pos = -1
    for x in range(size):
        if s in slst:
            pos = x
    print(pos)

search("abc", ["erm", "jfk", "lid", "abc", "doe"], 5)
        
