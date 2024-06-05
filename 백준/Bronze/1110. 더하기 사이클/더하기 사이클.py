import sys

inp = temp = int(input())
count = 0

while True:
    n1 = int(temp//10)
    n2 = int(temp%10)
    new_n = int(n1+n2)
    temp = int(n2*10 + new_n%10)
    count += 1
           
    if temp == inp:
        break    
print(count)