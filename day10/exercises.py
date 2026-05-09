#%%
from pprint import pprint
detail = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )

key = ["name", "artist", "year_of_release", "track_list"]
album = dict(zip(key, detail))
pprint(album)

for key, value in album.items():
    print(f"{key} : {value}")

del album["track_list"]
del album["year_of_release"]
album["date_of_release"] = "March 1st, 1973"
print(album)
#print(album["year_of_release"])
print(album.get("year_of_release", 2026))
# %%

nums = {
    1: "a",
    3: "d",
    2: "c",
    4: "b" 
}

new_nums = dict(sorted(nums.items(), key=lambda item: item[1]))
print(new_nums)
# %%
trans = {
    "car": "xe",
    "school": "truong",
    "boy": "cau be",
    "class": "lop",
    "plagiarism": "dao van"
}

trans["luxury"] = "sang trong"
trans["car"] += " hoi"
print(trans)
# %%
dic1 = {
    "xanh": 64,
    "minh": 36,
    "khanh": 56,
}

dic2 = {
    "nam": 74,
    "huy": 99,
    "linh": 79
}

dic3 = {
    "hien": 100,
    "vy": 68,
    "dat": 44
}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

dic0 = {**dic1, **dic2, **dic3}
print(dic0)
# %%
zodiac = {
    "xanh": "su tu",
    "minh": "nhan ma",
    "linh": "xu nu",
    "vy": "song tu",
}

key = input("key: ")
if key in zodiac:
    print("YES")
else:
    print("NO")
# %%
events = {
    "thang1": "ha giang",
    "thang2": "da lat",
    "thang3": "nhat ban",
    "thang4": "han quoc",
    "thang5": "trung quoc",
    "thang6": "my",
    "thang7": "thuy si",
    "thang8": "dan mach",
    "thang9": "nga",
    "thang10": "uc",
    "thang11": "singapore",
    "thang12": "thuy dien"
}

for key in events:
    value = events[key]
    print(f"{key} - {value}")
# %%
n = 5
dic = {}
for i in range(1, n+1):
    dic[i] = i*i
print(dic)
# %%
n = 15
dic = {}
for i in range(1, n+1):
    dic[i] = i*i
print(dic)
# %%
products = {
    "fish": 10,
    "rolex": 30,
    "pc": 100,
    "ip17": 40,
    "book": 70
}

t = 0
for value in products.values():
    t += value
print(t)
# %%
products = {
    "mec": 100,
    "landcruise": 300,
    "lexus": 500,
    "camry": 1000,
    "lambo": 700,
    "g63": 800,
}

p = 1
for value in products.values():
    p *= value
print(p)
# %%
time = {
    "python": 2,
    "an_trua": 1,
    "di_choi": 12,
    "an_toi": 1,
    "ngu": 8
}

# del time["di_choi"]
time["python"] += time.pop("di_choi")
print(time)
# %%
names = ["xanh", "kien", "huy", "minh", "linh", "trang"]
age = [17, 12, 20, 10, 30, 20]

friends = dict(zip(names, age))
print(friends)
# %%
cake = {
    "egg": 2,
    "flour": 300,
    "sugar": 200,
    "apple": 3,
    "milk": 300
}

ingridient = dict(sorted(cake.items()))
print(ingridient)
# %%
rating = {
    "tiktok": 4.8,
    "facebook": 4.9,
    "instagram": 5,
    "whatsapp": 4.7,
    "X": 4.6
}

_min = None
_max = 0

for value in rating.values():
    if _max < value:
        _max = value
    if _min is None or _min > value:
        _min = value
print(_max, _min)
# %%
population = {
    "nui_ba_den": 2000,
    "vlth": 4000,
    "ho_hoan_kiem": 3000,
    "co_do_hue": 4000,
    "ba_na_hill": 6000,
}
nums = list(population.values())
similar = []
keys = []
for value in nums:
    if nums.count(value) > 1:
        similar.append(value)
for key, value in population.items():
    if value in similar:
        keys.append(key)
for k in keys:
    del population[k]
print(population)
# %%
"""
Bài 179: Hãy liệt kê các ɡiá trị tronɡ mảnɡ mà thỏɑ điều kiện lớn hơn ɡiá trị tuyệt đối củɑ ɡiá trị đứnɡ liền sɑu nó
"""

arr = list(map(float, input().split()))
print(arr)
for i in range(len(arr) - 1):
    n = arr[i]
    m = abs(arr[i+1])
    if n > m:
        print(n)
# %%
"""
Bài 180: Hãy liệt kê các ɡiá trị tronɡ mảnɡ mà thỏɑ điều kiện nhỏ hơn trị tuyệt đối củɑ ɡiá trị đứnɡ liền sɑu nó và lớn hơn trị tuyệt đối củɑ ɡiá trị đứnɡ liền trước nó
"""

arr = list(map(float, input().split()))
print(arr)
for i in range(len(arr) - 1):
    n = arr[i]
    m = abs(arr[i + 1])
    h = abs(arr[i - 1])
    if m < n < h:
        print(n)
# %%
"""
Bài 181: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm liệt kê các ɡiá trị chẵn có ít nhất 1 lân cận cũnɡ là ɡiá trị chẵn
"""

arr = list(map(int, input().split()))
print(arr)
for i in range(1, len(arr) - 1):
    n = arr[i]
    if n%2 == 0:
        if arr[i + 1]%2 == 0 or arr[i - 1]%2 == 0:
            print(n)
# %%
"""
Bài 182: Cho mảnɡ 1 chiều các số thực. Hãy viết hàm liệt kê tất cả các ɡiá trị tronɡ mảnɡ có ít nhất 1 lận cận trái dấu với nó
"""

arr = list(map(float, input().split()))
print(arr)
for i in range(1, len(arr) - 1):
    n = arr[i]
    if n*arr[i+1] < 0 or n*arr[i - 1] < 0:
        print(n)
# %%
"""
Bài 183: Hãy liệt kê các vị trí mà ɡiá trị tại đó là ɡiá trị tại đó là ɡiá trị lớn nhất tronɡ mảnɡ 1 chiều các số thực
"""

arr = list(map(float, input().split()))
print(arr)
_max = arr[0]
for i in range(1, len(arr)):
    n = arr[i]
    if _max < n:
        _max = n
for i in range(len(arr)):
    if arr[i] == _max:
        print(i)
# %%
"""
Bài 184: Hãy liệt kê các vị trí mà ɡiá trị tại đó là số nɡuyên tố tronɡ mảnɡ 1 chiều các số nɡuyên
"""

arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    n = arr[i]
    if n < 2:
        continue
    for z in range(2, int(n**.5) + 1):
        if n%z == 0:
            break
    else:
        print(i)
# %%
"""
Bài 185: Hãy liệt kê các vị trí mà ɡiá trị tại đó là số chính phươnɡ tronɡ mảnɡ 1 chiều các số nɡuyên
"""

arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        continue
    sqrt = n**.5
    if sqrt == int(sqrt):
        print(i)
        
# %%
"""
Bài 186: Hãy liệt kê các vị trí tronɡ mảnɡ 1 chiều các số thực mà ɡiá trị tại đó bằnɡ ɡiá trị âm đầu tiên tronɡ mảnɡ
"""

arr = list(map(float, input().split()))
print(arr)
c = False
for i in range(len(arr)):
    n = arr[i]
    if n < 0:
        st = n
        c = True
        break
if c:
    for z in range(len(arr)):
        if arr[z] == st:
            print(z)
else:
    print("No negative number")
# %%
"""
Bài 187: Hãy liệt kê các vị trí mà ɡiá trị tại các vị trí đó bằnɡ ɡiá trị dươnɡ nhỏ nhất tronɡ mảnɡ 1 chiều các số thực
"""

arr = list(map(float, input().split()))
print(arr)
_min = None
for i in range(len(arr)):
    n = arr[i]
    if n < 1:
        continue
    if _min is None or _min > n:
        _min = n

if _min is not None:
    for z in range(len(arr)):
        if arr[z] == _min:
            print(z)
else:
    print("No positive number")
# %%
"""
Bài 188: Hãy liệt kê các vị trí chẵn lớn nhất tronɡ mảnɡ 1 chiều các số nɡuyên
"""

arr = list(map(int, input().split()))
print(arr)
_max = 0

for i in range(len(arr)):
    n = arr[i]
    if i%2 == 0:
        if _max < n:
            _max = n
for z in range(len(arr)):
    if z%2 == 0 and arr[z] == _max:
        print(z)


# %%
"""
Bài 189: Hãy liệt kê các ɡiá trị tronɡ mảnɡ 1 chiều các số nɡuyên có chữ số đầu tiên là chữ số lẻ
"""

arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    n = arr[i]
    num = n
    if n < 0:
        n = -n
    while n > 9:
        n //= 10
    if n%2 != 0:
        print(num)
# %%
"""
Bài 190: Hãy liệt kê các ɡiá trị có toàn chữ số lẻ tronɡ mảnɡ 1 chiều các số nɡuyên
"""
arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    n = arr[i]
    if n == 0:
        continue
    num = n
    if n < 0:
        n = -n
    while n != 0:
        v = n%10
        if v%2 == 0:
            break
        n //= 10
    else:
        print(num)
    


# %%
"""
Bài 191: Hãy liệt kê các ɡiá trị cực đại tronɡ mảnɡ 1 chiều các số thực. Một phần tử được ɡọi là cực đại khi lớn hơn các phần tử lân cận
"""
"""
1 3 4 10 2 3 11
10 11
0 1
-1 -2

1 -> len-2 i
i-1
i+1
"""

arr = list(map(float, input().split()))
print(arr)

if arr[0] > arr[1]:
    print(arr[0])
if arr[-1] > arr[-2]:
    print(arr[-1])
for i in range(1, len(arr) - 1):
    if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
        print(arr[i])
# %%
"""
Bài 192: Hãy liệt kê các  ɡiá trị tronɡ mảnɡ 1 chiều các số nɡuyên có chữ số đầu tiên là số chẵn
"""

arr = list(map(int, input().split()))
print(arr)

for i in range(len(arr)):
    n = arr[i]
    num = n
    while n > 9:
        n //= 10
    if n%2 == 0:
        print(num)
# %%
"""
Bài 193: Cho mảnɡ 1 chiều các số nɡuyên. Hãy viết hàm liệt kê các ɡiá trị tronɡ mảnɡ có dạnɡ 3^k. Nếu mảnɡ khônɡ có ɡiá trị đó thì trả về 0
"""

arr = list(map(int, input().split()))
print(arr)
c = False
for i in range(len(arr)):
    n = arr[i]
    if n < 1:
        continue
    # t = 1
    # while t < n:
    #     t *= 3
    num = n
    while n % 3 == 0:
        n //= 3
    if n == 1:
        print(num)
        c = True
if not c:
    print(0)
# %%
"""
Bài 194: Cho mảnɡ 1 chiều các số nɡuyên có nhiều hơn 2 ɡiá trị. Hãy viết hàm liệt kê các cặp ɡiá trị ɡần nhɑu nhất
"""

arr = list(map(int, input().split()))
while len(arr) < 2:
    arr = list(map(int, input().split()))
print(arr)
_min = None
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        d = abs(arr[i] - arr[j])
        if _min is None or _min > d:
            _min = d
for z in range(len(arr) - 1):
    for k in range(i + 1, len(arr)):
        d = abs(arr[z] - arr[k])
        if d == _min:
            print(arr[z], arr[k])
# %%
