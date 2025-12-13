n= int(input())
c=0
for i in range(n):
    m=input()
    if '++' in m:
        c+=1
    elif '--' in m:
        c-=1
print(c)
