n=int(input())
for i in range(n):
    m=input()
    if len(m)>10:
        print(m[0]+str(len(m)-2)+m[len(m)-1])
    else:
        print(m)