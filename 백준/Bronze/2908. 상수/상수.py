n1, n2 = map(str, input().split())
n1_rev = ''
n2_rev = ''

for char in n1:
    n1_rev = char + n1_rev
for char in n2:
    n2_rev = char + n2_rev

if int(n1_rev) > int(n2_rev):
    print(n1_rev)
else:
    print(n2_rev)