arr = list(map(float, input().split()))
_max = None

for i in range(len(arr)):
    if arr[i] < 0:
        if _max is None:
            _max = arr[i]
        else:
            if arr[i] > _max:
                _max = arr[i]
if _max is None:
    print(-1)
else:
    print(arr[i])