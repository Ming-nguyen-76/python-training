""" a = [1, 2, 3, 10, 12, 15]
# [2, 4, 6]

new = []

for x in a:
    if x%2 == 0:
        new.append(x)
print(new)
new = [x for x in a if x%2 == 0]
# print(x)

print(new)
 """

# a = [1, 2, 3]
# # [2, 6, 6]
# new = []
# for x in a:
#     if x%2 == 0:
#         new.append(3*x)
#     else:
#         new.append(2*x)
# print(new)

# new = [x*3 if x % 2 == 0 else x*2 for x in a]
# print(new)

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                lst.append([i, j, k])

print(lst)

lst = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

"""
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 2], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
"""

print(lst)