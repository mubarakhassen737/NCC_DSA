m = int(input())
n = str(m)

if len(n) == 4 or len(n) == 7:
    for i in n:
        if i != '4' and i != '7':
            print('NO')
            break
    else:  # Runs only if the loop didn't break
        print('YES')
else:
    print('NO')