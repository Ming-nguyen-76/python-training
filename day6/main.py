# %%
movies = [
    ("Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004),
    ("Memento",
        "Christopher Nolan",
        2000),
    ("Requiem for a Dream",
        "Darren Aronofsky",
        2000)
]

for film in movies:
    print(f"{film[0]} ({film[2]}), by {film[1]}")

# %%
movies = [
    ("Batman", "Me", 2000),
    ("Spiderman", "You", 2001),
    ("Ironman", "Him", 2002)
]

for film in movies:
    if film[2] == 2000:
        print("Batman is in the library")
        break
# %%
print(range(10, 0, -1))
# %%
for number in range(0, 9):
    print("Hi")
# %%
"""
for loop
"""
for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(i, "hello")

# %%
"""
break
continue
"""
for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
    if i % 2 == 0:
        continue
    print(i)

# %%
# nested loop
"""

"""
for i in range(3):  # i - 0 1 2

    if i == 1:
        continue

    for j in range(4):  # j - 0 1 2 3

        if j % 2 == 0:
            break

        print(i, j)

# %%
a = [1, 10, 3, -100]  # value
#    0   1  2    3     index
for number in a:
    print(number)

# 0 1 2 3
"""
len a = 4
0 -> 3
0 1 2 3 = range(4) = range(len)
"""

"""
0 | 1
1 | 10
2 | 3
3 | -100
"""
for i in range(len(a)):
    # print(i, end=" ")
    print(i, a[i], sep=' | ')
# %%
friends = ("Xanh", "Minh", "Huy", "Hoang Anh", "Minh Anh",
           "Tram Anh", "Bao Anh", "Tuan Anh", "Van Anh", "Trung")
print(len(friends))
for name in friends:
    lst = name.split()
    if lst[-1][0] == "A" or lst[-1][0] == "a":
        print(name)


# %%
movies = [("Batman", "Me", 2004),
          ("Spiderman", "You", 2005),
          ("Superman", "Him", 2003)
          ]
for movie in movies:
    print(f"{movie[0]} ({movie[2]}), by {movie[1]}")
# %%
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for employee in employees:
    money = employee[1]*employee[2]
    print(f"{employee[0]}: ${money}")
# %%
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total = count = 0
for emp in employees:
    # total = total + emp[2]
    total += emp[2]
    count += 1

average = total/count

for e in employees:
    if e[2] > average:
        print(e[0])

# %%
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total = 0
for emp in employees:
    total += emp[2]

average = total/len(employees)
for e in employees:
    if e[2] > average:
        print(e[0])
# %%
# Bai 1
"""
S(n) = 1 + 2 + 3 + ... + n

input: n int > 0
output: S(n)

S(3) = 1 + 2 + 3 = 6
S(4) = 1 + 2 + 3 + 4 = S(3) + 4 = 6 + 4 = 10

1. input n
1.1. t = 0
2. for i: 1 -> n
3.      t (new) = t (old) + i (cummulative)
4. print t
"""
n = int(input("n = "))

s = 0

for i in range(1, n + 1):
    s = s + i

print(f"S({n}) = {s}")

s = n*(n+1)//2
print(f"S({n}) = {s}")

# %%
# Bai 2
"""
S(n) = 1^2 + 2^2 + 3^2 + ... + n^2

input: n int > 0
output: S(n)

S(2) = 1^2 + 2^2 = 5
S(3) = 1^2 + 2^2 + 3^2 = 14

1. input n
1.1 s = 0
2. for i: 1 -> n
3. s(new) = s(old) + i*i
4. print s
"""

n = int(input("n = "))
s = 0
"""
range(1, n+1) = 1 -> n
range(n)      = 0 -> n-1
"""
for i in range(n):
    s += (i+1)**2

print(f"S({n}) = {s}")
# %%
# Bai 3
"""
S(n) = 1 + 1/2 + 1/3 + ... + 1/n

input: n int > 0
output: S(n)

S(2) = 1 + 1/2 = 1.5
S(3) = 1 + 1/2 + 1/3 = 1.83

1. input n
1.1 s = 0
2. for i: 1 -> n
3. s(new) = s(old) + 1/i
4. print rounded s
"""

n = int(input("n = "))
s = 0
for i in range(1, n + 1):
    s += 1/i
"""
1.34567 -> 1.35
round
1 -> 1.00
"""
print(f"S({n}) = {s:.2f}")
# %%
# Bai 4
"""
S(n) = 1/2 + 1/4 + ... + 1/2n

input: n int > 0
output: S(n)

S(2) = 1/2 + 1/4 = 0.75
S(3) = 1/2 + 1/4 + 1/6 = 0.92

1. input n
1.1 s = 0
2. for i: 1 -> n
3. s(new) = s(old) + 1/(2*i)
4. print rounded s
"""

n = int(input("n = "))
s = 0
for i in range(1, n + 1):
    s += 1/(2*i)

print(f"S({n}) = {s:.2f}")
# %%
# Bai 5
"""
S(n) = 1 + 1/3 + 1/5 + ... + 1/2n+1

input: n int >= 0
output: S(n)

S(2) = 1 + 1/3 + 1/5 = 1.53
S(3) = 1 + 1/3 + 1/5 + 1/7 = 1.68

1. input n
1.1 s = 0
2. for i: 0 -> n
3. s(new) = s(old) + 1/(2*i + 1)
4. print rounded s

1 3 5 7 ... 2i+1
"""

n = int(input("n = "))
s = 0
for i in range(1, 2*n+2, 2):
    s += 1/i

print(f"S({n}) = {s:.2f}")
#%%
# Bai 6
"""
S(n) = 1/1*2 + 1/2*3 + ... + 1/n*(n+1)

input: n int > 0
output: S(n)

S(2) = 1/1*2 + 1/2*3 = 0.67
S(3) = 1/1*2 + 1/2*3 + 1/3*4 = 0.75

1. input n
1.1 s = 0
2. for i: 1 -> n
3. s(new) = s(old) + 1/(i*(i + 1))
4. print rounded s
"""
n = int(input("n = "))
s = 0
for i in range(1, n + 1):
    s += 1/(i*(i + 1))

print(f"S({n}) = {s:.2f}")

#%%
# Bai 7
"""
S(n) = 1/2 + 2/3 + 3/4 ... + n/n+1

input: n int > 0
output: S(n)

S(2) = 1/2 + 2/3 = 1.17
S(3) = 1/2 + 2/3 + 3/4 = 1.92

1. input n
1.1 s = 0
2. for i: 1 -> n
3. s(new) = s(old) + i/(i + 1)
4. print rounded s
"""
n = int(input("n = "))
s = 0
for i in range(1, n +1):
    s += i/(i + 1)

print(f"S({n}) = {s:.2f}")
# %%
# Bai 8
"""
S(n) = 1/2 + 3/4 + 5/6 ... + 2n+1/2n+2

input: n int >= 0
output: S(n)

S(2) = 1/2 + 3/4 + 5/6 = 2.08
S(3) = 1/2 + 3/4 + 5/6 + 7/8 = 2.96

1. input n
1.1 s = 0
2. for i: 0 -> n 
3. s(new) = s(old) + 2*i + 1/(2*i + 2)
4. print rounded s
"""

n = int(input("n = "))
s = 0
for i in range(0, n + 1):
    s += (2*i + 1)/(2*i + 2)

print(f"S({n}) = {s:.2f}")
# %%
# Bai 9
"""
T(n) = 1*2*3*...*n

input: n int > 0
output: T(n)

T(2) = 1*2 = 2
T(3) = 1*2*3 = 6

1. input n
1.1 t = 1
2. for i: 0 -> n
3. t(new) = t(old)*i
4. print t
"""

n = int(input("n = "))
t = 1
for i in range(2, n + 1):
    t *= i

print(f"T({n}) = {t}")
# %%
# Bai 10
"""
T(x,n) = x^n

input: n int > 0
       x int >=0
output: T(x, n)

T(2, 2) = 2**2 = 4
T(3, 3) = 3**3 = 27

1. input x, n
1.1 t = 1
2. for i: 0 -> x
3. for j: 1 -> n
4. t(new) = i**j
5. print t

x^3 = x.x.x
x^5 = x.x.x.x.x

"""

x = float(input("x = "))
n = int(input("n = "))
t = 1
# for i in range(0, x + 1):
#     for j in range(1, n + 1):
#         t = i**j
r = 1

for _ in range(n):
    r *= x


print(f"T({x}, {n}) = {r}")
# %%
n = int(input("Enter a number: "))

for number in range(1, n + 1):
    if number % 15 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
# %%
"""
S(n) = x + x^2/2! + x^3/3! + … + x^n/N!

3! = 3x2! - i = 3
2! = 2x1! - i = 2
1! = 1 - p = 1
input: x(float), n(int > 0)
output: S(x, n)

S(3, 2) = 3 + 3^2/2! = 7.5
S(3, 4) = 3 + 3^2/2! + 3^3/3! + 3^4/4! = 15.38


1. input x, n
1.1 s = 0
2. for i range(1, n+1)
3.      t = 1
        for z range(2, i + 1)
            t = t*z
4.      s(new) = s(old) + x^i/t
5. print s
"""

x = float(input("x = "))
n = int(input("n = "))
s = 0

p = 1

for i in range(1, n + 1):
    # t = 1
    # for z in range(2, i + 1):
    #     t *= z
    p *= i
    s += x**i/p
print(f"S({x}, {n}) = {s:.2f}")
# %%
"""
n = 6
1 2 3 6

input: n(int > 0)
output: list

1. input n
1.1 lst = []
2. for num range(1, n + 1)
3.      if n%num == 0:
            lst.append(num)
    print(lst)
"""
"""
n = 16
a b
1 16
2 8
4 4
5 

axb = n
a <= b
a*a <= a*b
a^2 <= n
1 <= a <= sqrt(n)
b = n/a
a != b
"""

n = int(input("n = "))
lst = []

for a in range(1, int(n**.5) + 1):
    if n%a == 0:
        lst.append(a)
        b = n//a

        if a != b:
            lst.append(b)
lst.sort()
print(*lst, sep=', ')
# %%
"""
Tính tổnɡ tất cả các “ ước số” củɑ số nɡuyên dươnɡ n
input: n(int > 0)
output: sum of factor of n

n = 6
t = 12

n = 13
t = 14

1. input n
1.1 t = 0
2. for a range(1, int(n**.5) + 1)
3.      if n%a == 0
            t += a
            b = n//a

            if a!= b:
                t += b
4. print(t)

"""

n = int(input("n = "))
t = 0

for a in range(1, int(n**.5) + 1):
    if n%a == 0:
        t += a
        b = n//a

        if a != b:
            t += b
print(t)
# %%
"""
Tìm ước số lẻ lớn nhất củɑ số nɡuyên dươnɡ n

input: n(int > 0)
output: highest odd factor of n

n = 100
fact = 25

n = 13
fact = 13

1. input n
1.1 max = 1
2. for a in range(2, int(n**.5) + 1):
        if n%a == 0 and a%2 == 1
            if max < a
                max = a
            b = n//a

            if a != b and b%2 == 1
                if max < b
                    max = b
    print(max)
    
"""

n = int(input("n = "))
_max = 1

if n < 0:
    n = -n

for a in range(1, int(n**.5) + 1):
    if n%a == 0: 
        print(a, end=' ')
        if a%2 == 1 and _max < a:
            _max = a
        b = n//a
        print(b, end=' ')
        if a != b and b%2 == 1:
            if _max < b:
                _max = b
print()
print(_max)
# %%
"""
Cho số nɡuyên dươnɡ n. Tính tổnɡ các ước số nhỏ hơn chính nó

input: n(int > 0)
output: sum of factor < n

n = 6
a = 6

n = 13
a = 1

1. input n
1.1 t = 0
2. for a in range(1, int(n**.5) + 1)
        if n%a == 0:
            t += a
            b = n//a
            if b != a:
                t += b
    print(t - n)        
"""

n = int(input("n = "))
t = 1

for a in range(2, int(n**.5) + 1):
    if n%a == 0:
        t += a
        b = n//a
        if b != a:
            t += b
print(t)
# %%
"""
Cho số nɡuyên dươnɡ n. Kiểm trɑ xem n có phải là số hoàn thiện hɑy khônɡ

input: n(int > 0)
output: "YES"/ "NO"

n = 6
YES
n = 10
NO

1. input n
1.1 t = 1
2. for a range(2, int(n**.5) + 1)
        if n%a == 0:
            t += a
            b = n//a
            if b != a:
                t += b
    if t == n:
        print("YES")
    else: 
        print("NO")
"""

n = int(input("n = "))
t = 1

for a in range(2, int(n**.5) + 1):
    if n%a == 0:
        t += a
        b = n//a
        if b != a:
            t += b
if t == n:
    print("YES")
else:
    print("NO")
# %%
"""
Cho số nɡuyên dươnɡ n. Kiểm trɑ xem n có phải là số nɡuyên tố hɑy khônɡ

input: n(int > 0)
output: "YES"/ "NO"

n = 13
YES

n = 28
NO

1. input n
2. for a range(2, int(n**.5) + 1):
        if n%a == 0
            print("NO")
            break
    else:
        print("YES")
"""
n = int(input("n = "))

if n < 2:
    print("NO")
else:
    for a in range(2, int(n**.5) + 1):
        if n%a == 0:
            print("NO")
            break
    else:
        print("YES")

# %%
"""
Cho số nɡuyên dươnɡ n. Kiểm trɑ xem n có phải là số chính phương hɑy khônɡ

input: n(int > 0)
output: "YES"/ "NO"

n = 4
YES
n = 6
NO

1. input n
2. s = n**.5
3. if int(s) == s
        print("YES")
    else:
        print("NO")
"""

n = int(input("n = "))
if n > 0:
    s = n**.5

    if int(s) == s:
        print("YES")
    else:
        print("NO")
else:
    print("Invalid input")
# %%
