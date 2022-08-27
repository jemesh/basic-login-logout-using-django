arr=[10,5,2,7,1,9]
k=15
n=6
y = 0
j = 0
p = 0
for i in range(n):
    y += arr[i]
    if y == k:
        p = max(p, i - j + 1)
    elif y > k:
        y -= arr[j]
        j += 1
print(p)