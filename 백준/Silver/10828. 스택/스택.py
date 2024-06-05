import sys

def push(x):
    stack.append(x)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()
    
def size():
    return len(stack)

def empty():
    if(not stack):
        return 1
    else:
        return 0
    
def top():
    if(not stack):
        return -1
    else:
        return stack[-1]
    
    
stack = []
for _ in range(int(input())):
    inp = sys.stdin.readline().split()
    
    if inp[0] == "push":
        push(inp[1])
    elif inp[0] == "pop":
        print(pop())
    elif inp[0] == "size":
        print(size())
    elif inp[0] == "empty":
        print(empty())
    elif inp[0] == "top":
        print(top())