n,h=map(int,input().split())
c=list(map(int,input().split()))
leng=n
for i in c:
    if i>h:
        leng+=1
print(leng)