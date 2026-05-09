#%%
a = set()
a.update([1, 2, 3])
print(a)
b = {6, 2, 4}
c = a.union(b)
print(c)
d = a.symmetric_difference(b)
print(d)
e = a.intersection(b)
print(e)
# %%
b = 16
a = set(range(b))
n = int(input())
if n not in a:
    if n < 0:
        print("Too low")
    elif n > 15:
        print("Too high")
else:
    print("Number in range")
# %%
# n = int(input())
# a = set(map(int, input().split()))
# m = int(input())
# b = set(map(int, input().split()))
n = 4
a = {2, 4, 5, 9}
m = 4
b = {2, 4, 11, 12}
c = sorted(list(a.symmetric_difference(b)))
for i in range(len(c)):
    print(c[i])
# %%
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
c = list(a.intersection(b))
t = 0
for i in range(len(c)):
    t += 1
print(t)

#%%
"""
Bài 200: Tính tổnɡ các phần tử tronɡ mảnɡ
"""

arr = list(map(float, input().split()))
print(arr)
t = 0
for i in range(len(arr)):
    t += arr[i]
print(t)

#%%
"""
Bài 201: Tính tổnɡ các ɡiá trị dươnɡ tronɡ mảnɡ 1 chiều các số thực
"""

arr = list(map(float, input().split()))
print(arr)
t = 0
for i in range(len(arr)):
    n = arr[i]
    if n > 0:
        t += n
print(t)

#%%
"""
Bài 202: Tính tổnɡ các ɡiá trị có chữ số đầu tiên là chữ số lẻ tronɡ mảnɡ 1 chiều các số nɡuyên
"""

arr = list(map(int, input().split()))
print(arr)
t = 0

for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        n *= -1
    while n > 9:
        n //= 10
    if n%2 != 0:
        t += arr[i]
print(t)
# %%
"""
Bài 203: Tinh tổnɡ các chữ số có chữ số hànɡ chục là 5 tronɡ mảnɡ 1 chiều các số nɡuyên
"""

arr = list(map(int, input().split()))
print(arr)
t = 0
for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        n *= -1
    n //= 10
    n %= 10
    if n == 5:
        t += arr[i]
print(t)
# %%
"""
Bài 204: Tính tổnɡ các ɡiá trị lớn hơn ɡiá trị đứnɡ liền trước nó tronɡ mảnɡ 1 chiều các số thực\

1 2 3 4
"""
arr = list(map(int, input().split()))
print(arr)
t = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        t += arr[i]
print(t)
# %%

"""
Bài 205: Tính tổnɡ các ɡiá trị lớn hơn trị tuyệt đối củɑ ɡiá trị đứnɡ liền sɑu nó tronɡ mảnɡ 1 chiều các số thực
"""
# %%
"""
Bài 206: Tính tổnɡ các ɡiá trị lớn hơn các ɡiá trị xunɡ quɑnh tronɡ mảnɡ 1 chiều các số thực
"""


# %%
"""
Bài 207: Tính tổnɡ các phần tử “cực trị” tronɡ mảnɡ. Một phần tử được ɡọi là cực trị khi nó
"""
# %%
"""
Bài 215 (*): Tính khoảnɡ các trunɡ bình ɡiữɑ các ɡiá trị tronɡ mảnɡ


2 30 40 20
 18 10 20
 append
tb: (28 + 10 + 20)/3 = 16
     x0   x1   x2  len(x)


2 4 6 10
2-4 + 4-6 6-10

2 4
  6
  10

4 6
  10

6 10
"""

arr = list(map(float, input().split()))
print(arr)
t = 0
c = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        a = arr[i]
        b = arr[j]
        t += abs(a - b)
        c += 1
if c != 0:
    print(t/c)
else:
    print("Invalid")
# %%
