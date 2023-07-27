
# problem 1 - prefix

str1 = input('Enter infix: ')
l = []

while str1 != '':
    l.append(str1)
    str1 = input('Enter infix: ')

print(l)

s = []
a = {'-': 1, '+': 1, '*': 2, '/': 2, '**': 3, '(': 4, ')': 4}

for i in a.keys():
    s.append(i)

print(s)

o = []
stack = []

def precedence(op):
    if op in ['-', '+']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '**':
        return 3
    return 0

for i in range(len(l)):
    if l[i] in s:  
        while stack and precedence(l[i]) <= precedence(stack[-1]):
            o.append(stack.pop())
        stack.append(l[i])
    else: 
        o.append(l[i])

while stack:
    o.append(stack.pop())

print(' '.join(o[::-1]))
