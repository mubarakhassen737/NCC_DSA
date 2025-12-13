n= int(input())
c=[]
for i in range(n):
    m=input()
    c.append(m)
for i in range(len(c)):
    if i%2==0:
        print(c[i])