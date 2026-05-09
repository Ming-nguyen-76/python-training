#%%
def add(x, y):
    print(x + y)


def subtract(x, y):
    print(x - y)


def multiply(x, y):
    print(x*y)


def divide(x, y):
    if y == 0:
        print("Invalid")
        return
    print(x/y)


print(divide(1, 0))
add(2, 3)
subtract(4, 4)
multiply(3, 5)
# %%
def f():
    return 1
    return 2

print(f())
# %%
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
 }

def print_show_info():
    title = tv_show["title"]
    year = tv_show["initial_release"]
    season = tv_show["seasons"]
    print(f"{title} ({year}) - {season} seasons")


print_show_info()
# %%
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

def print_show_info():
    title = tv_show["title"]
    year = tv_show["initial_release"]
    season = tv_show["seasons"]
    print(f"{title} ({year}) - {season} seasons")


for tv_show in series:
    print_show_info()
# %%
def check_palindrome(word):
    # x = "".join(reversed(word))
    # return x == word
    return word == word[::-1]


word = input().strip()
f = check_palindrome(word)

if f:
    print("YES")
else:
    print("NO")

# %%
def to_jaden_case(string):
    word = ""
    s = string.split()
    for i in s:
        i = i.capitalize()

to_jaden_case("How can mirrors be real if our eyes aren't real")
# %%
s = "How can mirrors be real if our eyes aren't real"
print(s.split())
# %%
s = "aren't"
print(s.capitalize())
# %%
print(bin(2))
# %%
n = 42
orig = n
b = ''

while n > 0:
    b = str(n % 2) + b
    n //= 2

b = b if b else '0'
print(b)
# %%
def simple_multiplication(number) :
    return number * (9 - number%2 == 0)
    return number * (8 if number % 2 == 0 else 9)
    if number%2 == 0:
        return number*8
    else:
        return number*9
# %%
def dna_to_rna(dna):
    rna = []
    for i in dna:
        if i == "T":
            rna.append("U")
        else:
            rna.append(i)
    return "".join(rna)
# %%
"""
Bài 216: Đếm số lượnɡ số chẵn tronɡ mảnɡ
"""

def count_num(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            count += 1
    return count


arr = list(map(int, input().split()))
print(count_num(arr))

# %%
"""
Bài 217: Đếm số dươnɡ chiɑ hết cho 7 tronɡ mảnɡ
"""

def count_num(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i]%7 == 0:
            count += 1
    return count


arr = list(map(int, input().split()))
print(count_num(arr))
# %%
"""
Bài 218: Đếm số đối xứnɡ tronɡ mảnɡ
"""

def count_num(numbers):
    count = 0
    for i in range(len(numbers)):
        dao = 0
        n = numbers[i]
        num = n
        while n != 0:
            dao = dao*10 + n%10
            n //= 10
        if dao == num:
            count += 1
    return count


arr = list(map(int, input().split()))
print(arr)
print(count_num(arr))
# %%
"""
Bài 219: Đếm số lần xuất hiện củɑ ɡiá trị x tronɡ mảnɡ
"""
def count_num(nums, x):
    count = 0
    for i in range(len(nums)):
        if nums[i] == x:
            count += 1
    return count

x = int(input())
arr = list(map(int, input().split()))
print(arr)
print(count_num(arr, x))
# %%
