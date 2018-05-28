def neg_num(lst):
    negs = None
    for i in lst:
        while not negs:
            if lst[i] > 0:
                negs = lst[i]
    print(negs)




neg_num([2, 4, 5, 1, 4, 7, -1, 3, -2])
