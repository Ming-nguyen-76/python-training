arr = list(map(float, input().split()))
print(arr)
_min = None
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        a = arr[i]
        b = arr[j]
        d = abs(a - b)
        if _min is None:
            _min = d
        elif _min >= d:
            _min = d

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        a = arr[i]
        b = arr[j]
        d = abs(a - b)
        if d == _min:
            print(a, b)