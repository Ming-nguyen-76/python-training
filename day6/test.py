# %%
x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = []
for i in range(0, x):
    for j in range(0, y):
        for k in range(0, z):
            if i + j + k != n:
                lst.append([i, j, k])

print(lst)

# %%
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# %%
newlist = [x for x in range(10)]
# %%
x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = [[i, j, k] for i in range(x+1)for j in range(y+1)
       for k in range(z+1)if (i + j + k) != n]
print(lst)
# %%
n = int(input())
arr = map(int, input().split())


# %%
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append(name, score)

print(lst)


# %%
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()


# %%
