"""
    Reference: https://www.codewars.com//kata/5f7a715f6c1f810017c3eb07
"""


stack = [0]
end = stack

def start(f):
    stack.clear()
    return f

def push(n):
    if type(n) is int:
        stack.append(n)
    return push if type(n) is int else n

def add(f):
    stack.append(stack.pop() + stack.pop())
    return int(f[0]) if type(f) is list else f

def sub(f):
    stack.append(stack.pop() - stack.pop())
    return int(f[0]) if type(f) is list else f

def mul(f):
    stack.append(stack.pop() * stack.pop())
    return int(f[0]) if type(f) is list else f

def div(f):
    stack.append(stack.pop() // stack.pop())
    return int(f[0]) if type(f) is list else f
