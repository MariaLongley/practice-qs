def perfect_num(num):
    perfect_num_lst = []
    for x in range(1,num-1):
        sum = 0
        for i in range(1, x - 1):
            if x % i == 0:
                sum += i
        if sum == x:
            perfect_num_lst.append(x)
    print(perfect_num_lst)
            


perfect_num(500)
