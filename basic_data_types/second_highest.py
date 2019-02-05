if __name__ == '__main__':
    marks = []
    for _ in range(0,int(input())):
        name = input()
        score = float(input())
        marks.append([name,score])
    second_highest = sorted(list(set([marks for name, marks in marks])))[1]
    print('\n'.join([a for a,b in sorted(marks) if b == second_highest]))
