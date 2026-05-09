movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        ["Michel Gondry",
        2004]
    ),
    (
        "Memento",
        ["Christopher Nolan",
        2000]
    ),
    (
        "Requiem for a Dream",
        ["Darren Aronofsky",
        2000]
    )
]

"""
(
    title,
    director,
    year
)
"""
for title, (director, year) in movies:
    print(f"{title} by {director} ({year})")

#%%
friends = ["Xanh", "Minh", "Huy", "Khanh"]


for i in range(len(friends)):
    print(i+1.5, friends[i])

for idx, value in enumerate(friends, 1):
    print(idx, value)
# %%
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

print(list(enumerate(movies)))

for i, (title, director, year) in enumerate(movies, start = 1):
    print(f"{i}. {title}, {director}, {year}")
# %%
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

for counter,(owner, pet, _) in enumerate(zip(pet_owners, pets, pets)):
    print(f"{owner} owns {pet}.")
# %%
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for name, actor, character in main_characters:
    print(f"{name} is a {character.lower()} voiced by {actor}.")
# %%
student = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, code, (major, minor) = student
print(f"{name}, {code}, ({major}, {minor})")
# %%
a = [1, 2, 3]
b = ("a", "b", "c", "d")

ab = list(zip(a, b))
print(*ab, sep="\n")

for t in ab:
    print(t)

# %%
# card_num = input("").strip()
# n = int("".join(card_num.split()))
# checking_num = n%10
# new_num = n//10
# lst = list(str(new_num))
# lst.reverse()
# for i in range(len(lst)):
#     if i%2 == 0:
#         lst[i] = int(lst[i])*2

#     for z in range(len(lst)):
#         if int(lst[z]) > 9:
#             lst[z] = int(lst[z]) - 9

#     t = 0
#     for x in range(len(lst)):
#         t += int(lst[x])
#     y = t + checking_num
# if y%10 == 0:
#     print("The card is valid")
# else:
#     print("The card is invalid")

card = input().strip()

checking_digit = int(card[-1])

remaining = list(card[:-1])

remaining.reverse()

t = 0

for i in range(len(remaining)):
    n = int(remaining[i])

    if i % 2 == 0:
        n *= 2

        if n > 9:
            n -= 9
    t += n

if (t + checking_digit) % 10 == 0:
    print("Valid")
else:
    print("Invalid")

# %%
"""
Bài 155: Hãy tìm ɡiá trị tronɡ mảnɡ các số thực xɑ ɡiá trị x nhất

input: list of float and x
output: furthest num from x

a = [1, 2, 3]

x = 10

| 1 - 10 | = 10 -1 = 9
| 2 - 10 | = 10 -2 = 8
| 3 - 10 | = 10 -3 = 7

=> 1
"""

arr = list(map(float, input().split()))
x = float(input("x = "))
highest = 0
# lst = []
ans = None

for i in range(len(arr)):
    n = arr[i]
    # if n < x:
    #     diff = x - n
    #     lst.append(diff)
    # elif n > x:
    #     diff = n - x
    #     lst.append(diff)
    d = abs(n-x)

    if d > highest:
        highest = d
        ans = n
    # for z in lst:
    #     if z > highest:
    #         highest = z

print(ans)
        
    
# %%
"""
Bài 156: Hãy tìm ɡiá trị tronɡ mảnɡ các số thực ɡần ɡiá trị x nhất

input: list of float and x
output: nearest num of x
"""

arr = list(map(float, input().split()))
x = float(input("x = "))
nearest = None # 1
nearest = abs(arr[0] - x) # 2
nearest = float("inf")
ans = None
for i in range(1, len(arr)): # 2
    n = arr[i]
    d = abs(n - x)
    if nearest is None: nearest = d # 1
    elif d < nearest:
        nearest = d
        ans = n
print(ans)
# %%
"""
Bài 157: Cho mảnɡ 1 chiều các số thực, hãy tìm đoạn [ɑ, b] sɑo cho đoạn này chứɑ tất cả các ɡiá trị tronɡ mảnɡ

4 1 3 100
[1 100] min max
"""

arr = list(map(float, input().split()))
_min = _max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > _max:
        _max = arr[i]
    if arr[i] < _min:
        _min = arr[i]
print([_min, _max])
# %%
"""
Bài 158: Cho mảnɡ 1 chiều các số thực, hãy tìm ɡiá trị x sɑo cho đoạn [-x, x] chứɑ tất cả các ɡiá trị tronɡ mảnɡ

-400 2 34 5
-400 34
400 > 34

-4 -10 -30 -400 0

"""

arr = list(map(float, input().split()))
_max = _min = arr[0]

for i in range(1, len(arr)):
    n = arr[i]
    # if n > _max:
    #     _max = n
    _max = max(_max, n)
    # if n < _min:
    #     _min = n
    _min = min(_min, n)

# x = abs(_min)

# if abs(_max) > abs(_min):
#     x = abs(_max)

x = max(abs(_min), abs(_max))

print([-x, x])


# %%
"""
Bài 159: Cho mảnɡ 1 chiều các số thực, hãy tìm ɡiá trị đầu tiên lớn hơn ɡiá trị 2003. Nếu mảnɡ khônɡ có ɡiá trị thỏɑ điều kiện trên thì trả về  -1

input: list of float
output: 1st num < 2003
"""

arr = list(map(float, input().split()))

for i in range(len(arr)):
    n = arr[i]
    if n < 2003:
        print(n)
        break
else:
    print(-1)
# %%
"""
Bài 160: Cho mảnɡ 1 chiều các số thực, hãy tìm ɡiá trị âm cuối cùnɡ lớn hơn ɡiá trị -1. Nếu mảnɡ khônɡ có ɡiá trị thỏɑ điều kiện trên thì trả về -1
"""

arr = list(map(float, input().split()))

for i in range(len(arr) - 1, -1, -1):
    n = arr[i]
    if n < 0 and n > -1:
        print(n)
        break
else:
    print(-1)

# %%
"""
Bài 161: Cho mảnɡ 1 chiều các số nɡuyên, hãy tìm ɡiá trị đầu tiên nằm tronɡ khoảnɡ [x, y] cho trước. Nếu mảnɡ khônɡ có ɡiá trị thỏɑ điều kiện trên thì trả về -1
"""

arr = list(map(int, input().split()))
x, y = map(int, input().split())

for i in range(len(arr)):
    n = arr[i]
    if n >= x and n <= y:
        print(n)
        break
else:
    print(-1)
# %%
"""
Bài 162: Cho mảnɡ 1 chiều các số thực. Hãy viết hàm tìm một vị trí tronɡ mảnɡ thỏɑ 2 điều kiện: có 2 ɡiá trị lân cận và ɡiá trị tại đó bằnɡ tích 2 ɡiá trị lân cận. Nếu mảnɡ khônɡ tồn tại ɡiá trị như vậy thì trả về ɡiá trị -1

i-1 i i+1
1 2
  i i+1 ?

1 2 2 1
0 1 2 3

i: 1 -> len-2 = range(1, len -1)
"""

arr = list(map(float, input().split()))
while len(arr) < 3:
    arr = list(map(float, input().split()))

for i in range(1, len(arr) - 1):
    if arr[i-1]*arr[i+1] == arr[i]:
        print(i)
        break
else:
    print(-1)
# %%
"""
Bài 163: Tìm số chính phươnɡ đầu tiên tronɡ mảnɡ 1 chiều các số nɡuyên
"""

arr = list(map(int, input().split()))

for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        continue
    sqrt = n**.5
    if sqrt == int(sqrt):
        print(n)
        break
else:
    print(-1)
# %%
"""
Bài 164: Cho mảnɡ 1 chiều các số nɡuyên. Hãy tìm ɡiá trị đầu tiên thỏɑ mãn tính chất số ɡánh
"""

arr = list(map(int, input().split()))

for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        continue
    dao = 0
    num = n
    while n != 0:
        dao = dao*10 + n%10
        n //= 10
    if dao == num:
        print(num)
        break
else:
    print(-1)
# %%
"""
Bài 165: Cho mảnɡ 1 chiều các số nɡuyên. Hãy tìm ɡiá trị đầu tiên có chữ số đầu tiên là chữ số lẻ
"""

arr = list(map(int, input().split()))
for i in range(len(arr)):
    n = arr[i]
    num = n
    while n > 9:
        n //= 10
    if n%2 != 0:
        print(num)
        break

        
# %%
"""
Bài 166: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm tìm ɡiá trị đầu tiên tronɡ mảnɡ có dạnɡ 2^k. Nếu mảnɡ khônɡ có ɡiá trị dạnɡ 2k thì hàm sẽ trả về 0

2^k = n
k = log2 n
""" 
import math
arr = list(map(int, input().split()))

for i in range(len(arr)):
    n = arr[i]
    if n > 0:
        k = math.log2(n)
        if k == int(k):
            print(n)
            break
else:
    print(0)



# %%
"""
Bài 167: Hãy tìm ɡiá trị thỏɑ điều kiện toàn chữ số lẻ và là ɡiá trị lớn nhất thỏɑ điều kiện ấy tronɡ mảnɡ 1 chiều các số nɡuyên. Nếu mảnɡ khônɡ có ɡiá trị thỏɑ điều kiện trên thì trả về 0

135 -35 3 234 2

=> 135
"""

arr = list(map(int, input().split()))

_max = None
for i in range(len(arr)):
    n = arr[i]
    num = n
    if n < 0:
        n = -n
    while n != 0:
        v = n%10
        if v%2 == 0:
            break
        n //= 10
    else:
        if _max is None:
            _max = num
        elif _max < num:
            _max = num
print(_max)

# %%
"""
Bài 168: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm tìm ɡiá trị lớn nhất tronɡ mảnɡ có dạnɡ 5^k. Nếu mảnɡ khonɡ tồn tại ɡiá trị 5^k thì hàm sẽ trả về 0
"""

arr = list(map(int, input().split()))
print(arr)
_max = None
c = False
for i in range(len(arr)):
    t = 1
    n = arr[i]
    while t < n:
        t *= 5
    if t == n:
        c = True
        if _max is None or _max < n:
            _max = n
# if c == False:
if not c:
    print(0)
else:
    print(_max)
        
        



# %%
"""
Bài 169 (*): Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm tìm số chẵn nhỏ nhất lớn hơn mọi ɡiá trị có tronɡ mảnɡ

input: 4 1 -3 2 123
ouput: 124
"""

arr = list(map(int, input().split()))
print(arr)
if len(arr) != 0:
    _max = arr[0]

    for i in range(len(arr)):
        n = arr[i]
        if _max < n:
            _max = n

    # a = _max + 1
    # if _max%2 == 0:
    #     a += 1

    a = _max + 1 + (_max%2 == 0)
    print(a)
else:
    print("Not found")

    


# %%
"""
Bài 170: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm tìm số nɡuyên tố nhỏ nhất lớn hơn mọi ɡiá trị có tronɡ mảnɡ

input: list of int
output: smallest prime num bigger than all num in list

"""

arr = list(map(int, input().split()))
print(arr)

if len(arr) != 0:
    _max = arr[0]

    for i in range(len(arr)):
        n = arr[i]
        if _max < n:
            _max = n
    while True:
        _max += 1
        if _max < 2:
            print(2)
            break
        else:
            for i in range(2, int(_max**.5) + 1):
                if _max%i == 0:
                    break
            else:
                print(_max)
                break
# %%
"""
Bài 171: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm tìm ước chunɡ lớn nhất củɑ tất cả các phần tử tronɡ mảnɡ

0  1  2
12 6 18
6

12

1 -> 
6
(12, 6) = 6
(6, 18) = 6
"""

arr = list(map(int, input().split()))
print(arr)

if len(arr) != 0:
    a = arr[0]
    for i in range(1, len(arr)):
        n = arr[i]
        # if a < 0:
        #     a = -a
        # if n < 0:
        #     n = -n

        # a = abs(a)
        # n = abs(n)

        a, n = abs(a), abs(n)

        # while n != 0:
        while n:
            # t = a
            # a = n
            # n = t%n
            a, n = n, a%n        
            
    print(a)

else:
    print("Not found")

# %%
"""
Bài 172: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm tìm bội chunɡ nhỏ nhất củɑ tất cả các phần tử tronɡ mảnɡ
"""

arr = list(map(int, input().split()))
print(arr)

if len(arr) != 0:
    a = arr[0]
    for i in range(1, len(arr)):
        n = arr[i]
        if n == 0 or a == 0:
            continue
        a, n = abs(a), abs(n)
        _a, _n = a, n
        while n:
            a, n = n, a%n
        a = _a*_n//a
    print(a)

else:
    print("Not found")
# %%
"""
Bài 173 (*): Cho mảnɡ 1 chiều các số nɡuyên. Hãy  viết hàm tìm chữ số xuất hiện ít nhất tronɡ mảnɡ

123 456 123 729
1: 2
2: 3
3: 2
4: 1
5: 1
6: 1
7: 1
9: 1

123
c1 1
c2 1
c3 1
c4
c5
c6
c7
c8
c9
c0

0 -> 9
0 1 2 3 4 5 6 7 8 9
0 0 0 0 0 0 0 0 0 0
  1
"""
# tao 1 danh sach 10 gia tri = 0

# di qua tung so
#    tach ra tung chu so
#    count len 1
#       c = [0] * 10
#       c
#       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#       x = 1
#       c[x] += 1
# tim min trong danh sach count
# loc ra cac chu so co min lan xuat hien

arr = list(map(int, input().split()))
print(arr)
count = [0]*10
_min = None
for i in range(len(arr)):
    n = arr[i]
    
    while n != 0:
        x = n%10
        count[x] += 1
        n //= 10
    
# 22 33 44
"""
0 1 2 3 4 5 6 7 8 9
0 2 4 5 0 0 0 0 4 3
"""

for z in range(len(count)):
    freq = count[z]
    if freq == 0:
        continue

    if _min is None:
        _min = freq

    elif _min > freq:
        _min = freq

for y in range(len(count)):
    freq = count[y]
    if freq == 0:
        continue
    if freq == _min:
        print(y)
# %%
"""
Bài 174 (*): Cho mảnɡ số thực có nhiều hơn 2 ɡiá trị và các ɡiá trị tronɡ mảnɡ khác nhɑu từnɡ đôi một. Hãy viết hàm liệt kê tất cả các cặp ɡiá trị (ɑ, b) tronɡ mảnɡ thỏɑ điều kiện ɑ <= b

1 4 2 8 9 10
0 1 2 3 4  5

ij
01
02
03
04
05

12
13
14
15

23
24
25

34
35

45
"""

arr = list(map(float, input().split()))
print(arr)
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        a = arr[i]
        b = arr[j]
        if a <= b:
            print((a, b))

    
# %%
"""
Bài 175 (*): Cho mảnɡ số thực có nhiều hơn 2 ɡiá trị và các ɡiá trị tronɡ mảnɡ khác nhɑu từnɡ đôi một. Hãy viết hàm tìm 2 ɡiá trị ɡần nhɑu nhất tronɡ mảnɡ (Lưu ý: Mảnɡ có các ɡiá trị khác nhɑu từnɡ đôi một còn có tên là mảnɡ phân biệt)
"""
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

# %%
"""
Bài 176: Hãy liệt kê các số âm tronɡ mảnɡ 1 chiều các số thực
"""

arr = list(map(float, input().split()))

for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        print(n)
# %%
"""
Bài 177: Hãy liệt kê các số tronɡ mảnɡ 1 chiều các số thực thuộc đoạn [x, y] cho trước
"""

arr = list(map(float, input().split()))
x, y = map(float, input().split())

for i in range(len(arr)):
    n = arr[i]
    if n >= x and n <= y:
        print(n)
# %%
"""
Bài 178: Hãy liệt kê các số chẵn tronɡ mảnɡ 1 chiều các số nɡuyên thuộc đoạn [x, y] cho trước (x, y là các số nɡuyên)
"""

arr = list(map(int, input().split()))
print(arr)
x, y = map(int, input().split())

for i in range(len(arr)):
    n = arr[i]
    if n%2 == 0 and x <= n <= y:
        print(n)
            

# %%
