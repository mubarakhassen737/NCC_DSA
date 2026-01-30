n = int(input())
a = list(map(int, input().split()))

max_val = -1
max_idx = -1
for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
        max_idx = i

min_val = 101
min_idx = -1
for i in range(n):
    if a[i] <= min_val:
        min_val = a[i]
        min_idx = i

ans = max_idx + (n - 1 - min_idx)
if max_idx > min_idx:
    ans -= 1

print(ans)