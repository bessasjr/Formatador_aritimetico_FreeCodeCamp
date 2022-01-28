def arithmetic_arranger(problems, condition=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    y = len(problems)
    space = '    '
    num_one = []
    num_two = []
    results = []
    count = 0    

    for n in problems:
        n = n.split()

        if n[0].isdigit() == False or n[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        if len(n[0]) > 4 or len(n[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if n[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if len(n[0]) >= len(n[2]):
            t = (len(n[0]) - len(n[2])) + 1
            num_two.append((n[1]+' '*t+n[2]))

        else:
            t = (len(n[2]) - len(n[0])) + 1
            num_two.append((n[1]+' '*1+n[2]))

        s = (len(num_two[count]) - len(n[0]))
        num_one.append((' '*s+n[0]))

        if n[1] == '+':
            nn = int(n[0]) + int(n[2])
            nn = str(nn)
            q = (len(num_two[count]) - len(nn))
            results.append(' '*q+nn)
        elif n[1] == '-':
            nn = int(n[0]) - (int(n[2]))

            nn = str(nn)
            q = (len(num_two[count]) - len(nn))
            results.append(' '*q+nn)
        count = count + 1

    def one(n):
        return f'{num_one[n]}{space}'
    def one_f(n):
        return f'{num_one[n]}'        
    def two(n):
        return f'{num_two[n]}{space}'
    def two_f(n):
        return f'{num_two[n]}'
    def mark(n):
        return f'{"-"*(len(num_two[n]))}{space}'
    def mark_f(n):
        return f'{"-"*(len(num_two[n]))}'
    def res(n):
        return f'{results[n]}{space}'
    def res_f(n):
        return f'{results[n]}'

    if condition == True:
        if y == 5:
            arranged_problems = f'{one(0)}{one(1)}{one(2)}{one(3)}{one_f(4)}\n{two(0)}{two(1)}{two(2)}{two(3)}{two_f(4)}\n{mark(0)}{mark(1)}{mark(2)}{mark(3)}{mark_f(4)}\n{res(0)}{res(1)}{res(2)}{res(3)}{res_f(4)}'
        if y == 4:
            arranged_problems = f'{one(0)}{one(1)}{one(2)}{one_f(3)}\n{two(0)}{two(1)}{two(2)}{two_f(3)}\n{mark(0)}{mark(1)}{mark(2)}{mark_f(3)}\n{res(0)}{res(1)}{res(2)}{res_f(3)}'
        if y == 3:
            arranged_problems = f'{one(0)}{one(1)}{one_f(2)}\n{two(0)}{two(1)}{two_f(2)}\n{mark(0)}{mark(1)}{mark_f(2)}\n{res(0)}{res(1)}{res_f(2)}'
        if y == 2:
            arranged_problems = f'{one(0)}{one_f(1)}\n{two(0)}{two_f(1)}\n{mark(0)}{mark_f(1)}\n{res(0)}{res_f(1)}'
        if y == 1:
            arranged_problems = f'{one_f(0)}\n{two_f(0)}\n{mark_f(0)}\n{res_f(0)}'
    
    if condition is False:
        if y == 5:
            arranged_problems = f'{one(0)}{one(1)}{one(2)}{one(3)}{one_f(4)}\n{two(0)}{two(1)}{two(2)}{two(3)}{two_f(4)}\n{mark(0)}{mark(1)}{mark(2)}{mark(3)}{mark_f(4)}'
        if y == 4:
            arranged_problems = f'{one(0)}{one(1)}{one(2)}{one_f(3)}\n{two(0)}{two(1)}{two(2)}{two_f(3)}\n{mark(0)}{mark(1)}{mark(2)}{mark_f(3)}'
        if y == 3:
            arranged_problems = f'{one(0)}{one(1)}{one_f(2)}\n{two(0)}{two(1)}{two_f(2)}\n{mark(0)}{mark(1)}{mark_f(2)}'
        if y == 2:
            arranged_problems = f'{one(0)}{one_f(1)}\n{two(0)}{two_f(1)}\n{mark(0)}{mark_f(1)}'
        if y == 1:
            arranged_problems = f'{one_f(0)}\n{two_f(0)}\n{mark_f(0)}'
            
    return arranged_problems

