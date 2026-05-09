arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    n = arr[i]
    while n != 0:
        n //= 10
    if n%2 != 0:
        x = n
        print(z)

