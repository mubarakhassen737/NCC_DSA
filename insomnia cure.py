d=int(input())
n=int(input())
k=int(input())
l=int(input())
m=int(input())
count=0
for i in range(1,d+1):
    if i%n==0 or i%k==0 or i%l==0 or i%m==0:
        count+=1
print(count)