def multi_table(row,column):
    for r in range(row):
        for c in range(column):
            print((r+1)*(c+1), " ", end="")
        print("")

multi_table(2,3)
