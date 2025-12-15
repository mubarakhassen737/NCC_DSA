n=int(input())
for I in range(n):
    a,b,c=map(int,input().split())
    if c==a+b:
        print('+')
    elif c==a-b:
        print('-')    
        