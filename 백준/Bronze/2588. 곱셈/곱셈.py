a = int(input())
b = int(input())

num1 = a*((b%100)%10)
num2 = a*((b%100)//10)
num3 = a*((b//100))
total = a*b

print(num1, num2, num3, total, sep='\n')