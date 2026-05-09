a = [1, 3, 2, 1, 4]

# list
""" c = False
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print("YES")
            c = True
            break
if not c:
    print("NO") """

# set
seen = set()

for x in a:
    if x in seen:
        print("YES")
        break
    seen.add(x)
else:
    print("NO")