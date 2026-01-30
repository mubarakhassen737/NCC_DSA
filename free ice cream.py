n,x=map(int,input().split())
kids=0
for i in range(n):
    a,b=input().split()
    b=int(b)
    if a == '+':
        x+=b
    elif a== '-':
        if x>=b:
            x-=b
        else:
            kids+=1
            continue
print(x,kids)