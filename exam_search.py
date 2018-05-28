def exam_results(file_name):
    results = []
    with open(file_name) as stream:
        for line in stream:
            newline = line.rstrip().split(" ")
            results.append(tuple(newline[0], newline[1]))
    return results
            
def get_grade(results)   
    print("Please enter a name to search for the grade. (If you want to quit enter XXX.)")
    name = None
    size = len(results)
    while name != "XXX":
        name = input("Enter a name: ")
        grade_pos = search(name, results, size)
        if grade_pos == -1:
            print("The person you entered did not take this exam.")
        else:
            grade = results[grade_pos]
            print("Grade: ", grade[1])

def search(s, slst, size):
    pos = -1
    for x in range(size):
        if s in slst:
            pos = x
    print(pos)
