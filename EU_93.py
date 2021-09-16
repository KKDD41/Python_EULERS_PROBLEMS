import re  # регулярные выражения
from itertools import permutations
from itertools import combinations


# Приоритет операций-символов
def op_prior(o):
    if o == '*':
        return 4
    elif o == '/':
        return 3
    elif o == '%':
        return 2
    elif o == '+':
        return 1
    elif o == '-':
        return 1


def opn(expr: str):  # входной параметр -- инфиксная строка арифметического выражения с пробелами!!!
    co = []  # выходная строка
    stack = []  # стек операторов
    tokens = re.split('[ ]+', expr)  # разбиваем в список по пробелам
    for i in tokens:
        if i.isdigit():
            co.append(int(i))  # в стек
        elif i in ['*', '/', '%', '+', '-']:
            token_tmp = ''  # смотрим на вверх стека
            if len(stack) > 0:
                token_tmp = stack[-1]  # смотрим на вверх стека
                while len(stack) > 0 and token_tmp != '(':  # пока стек не пуст и не скобка
                    if op_prior(i) <= op_prior(token_tmp):  # сравнение приоритета
                        co.append(stack.pop())  # если в стеке операция выше,то выталкиваем его в выходную строку
                    else:
                        break
            stack.append(i)  # тогда выйдя из цикла,добавим операцию в стек
        elif i == '(':
            stack.append(i)
        elif i == ')':
            token_tmp = stack[-1]  # смотрим на вверх стека
            while token_tmp != '(':  # пока не всретим открывающию скобку
                co.append(stack.pop())
                token_tmp = stack[-1]  # смотрим на вверх стека внутри цикла
                if len(stack) == 0:
                    raise RuntimeError('V virajenii propushena (')
                if token_tmp == '(':
                    stack.pop()
    while len(stack) > 0:
        token_tmp = stack[len(stack) - 1]
        co.append(stack.pop())
        if token_tmp == '(':
            raise RuntimeError('V virajenii propushena )')
    return co  # вернем постфиксную запись


def count(post_expr: list):
    stack = []
    for i in post_expr:
        if i not in ['*', '/', '%', '+', '-']:
            stack.append(i)
        elif i in ['*', '/', '%', '+', '-']:
            x = stack.pop()
            y = stack.pop()
            if i == '/' and x == 0:
                return 0
            elif i == '+':
                stack.append(y+x)
            elif i == '-':
                stack.append(y-x)
            elif i == '*':
                stack.append(y*x)
            elif i == '/':
                stack.append(y/x)
    return stack[-1]


def length(S):
    l = 1
    while l in S:
        l += 1
    return l


def clean_list(P: list):
    P_clean = []
    for x in P:
        if x in P_clean:
            pass
        else:
            P_clean.append(x)
    return P_clean


operators = ['*', '*', '*', '/', '/', '/', '+', '+', '+', '-', '-', '-']
numbers = [range(10)]
longest = 0


for k in combinations(range(1, 10), 4):
    S = set()
    for i in permutations(k):
        for j in clean_list(permutations(operators, 3)):  # тут знаки различны, а должны повторяться
            a, b, c, d = i
            o1, o2, o3 = j
            if count([a, b, c, d, o1, o2, o3]) > 0:
                S.add(count([a, b, c, d, o1, o2, o3]))
            if count([a, b, c, o1, d, o2, o3]) > 0:
                S.add(count([a, b, c, o1, d, o2, o3]))
            if count([a, b, c, o1, o2, d, o3]) > 0:
                S.add(count([a, b, c, o1, o2, d, o3]))
            if count([a, b, o1, c, d, o2, o3]) > 0:
                S.add(count([a, b, o1, c, d, o2, o3]))
            if count([a, b, o1, c, o2, d, o3]) > 0:
                S.add(count([a, b, o1, c, o2, d, o3]))
    longest = max(longest, length(S))

print(longest)
