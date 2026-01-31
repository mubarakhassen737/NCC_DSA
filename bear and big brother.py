t=int(input())
alp=['YES','yEs','yes','Yes','yeS','YeS','yES','YEs']
for i in range(t):
    s=input()
    if s in alp:
        print('YES')
    else:
        print('NO')