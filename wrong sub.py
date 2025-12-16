k,n=map(int,input().split())
for i in range(n):
    if k%10!=0:
        k-=1
    else:
        k//=10    
print(k)