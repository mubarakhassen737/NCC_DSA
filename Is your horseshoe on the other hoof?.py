s = list(map(int, input().split()))
unique_colors = set(s)
print(4 - len(unique_colors))