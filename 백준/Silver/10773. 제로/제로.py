import sys

stack = []
for _ in range(int(input())):
    inp = int(sys.stdin.readline())
    if inp == 0:
        stack.pop()
    else:
        stack.append(inp)
print(sum(stack))