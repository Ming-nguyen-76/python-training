# %%
import math
a = [1, 2, 3]
print(str(a))

b = ["1", "2", 3]
new = []
for x in a:
    new.append(str(x))

"""
join - convert list to string
"""
print(", ".join(map(str, b)))

new = []
for x in a:
    new.append(str(x))
print(", ".join(new))

new = list(map(str, a))
print(new)
print(" | ".join(new))

# %%
# split - convert string to list[str]

new = input("Enter some numbers: ")
"""
1 2 3 4 - str

split

['1', '2', '3', '4']
"""

# "               1         2          3          "
list_str = new.split('')
print(list_str)  # ["1", "      2", "           3"]


# %%
# 1.
names = input("Enter your name and surname: ")

# list_name = names.split()
# name = list_name[0]
# surname = list_name[1]

name, surname = names.split()

print(name)
print(surname)
# %%
# 2.
lst = [1, 2, 3, 4, 5]
# new_lst = list(map(str, lst))
print(" | ".join(map(str, lst)))


# %%
# 3.
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",

    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",

    "'The very essence of romance is uncertainty.'",

    "'We are not here to do what has already been done.'"
]
for quote in quotes:
    # print(quote[1:-1])
    print(quote.strip("'"))

# %%
# 4.
word = input("Enter a word: ").strip()
characters = len(word)
print(characters)

sentence = input("Enter a sentence: ").strip()
word_count = len(sentence.split())
print(f"Word count: {word_count}")
# %%
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budget = 0
num_movies = 0
for movie in movies:
    total_budget += movie[1]
    num_movies += 1
avg = total_budget/num_movies
print(f"Avgerage of movies: ${avg:.2f}")

movie_higher = 0
for movie in movies:
    if movie[1] > avg:
        movie_higher += 1
        more_than = movie[1] - avg
        print(f"{movie[0]}, higher ${more_than} than average")
print(f"There are {movie_higher} movies higher than average")

# %%
"""
2^k = n
k = ?
k int => True

"""

x = int(input("Enter an integer: "))
k = math.log2(x)
if k == int(k):
    print("YES")
else:
    print("NO")

# %%
"""
input: a,b,c (float)
output: largest number

1. input a,b,c
1.1 max = a
if b > max:
    max = b

if c > max:
    max = c

print(max)


"""
a, b, c = map(float, input().split())
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
m = a
if b > m:
    m = b
if c > m:
    m = c
print(m)
# %%
"""
input: a, b (float)
output:"YES"/"NO"

1. input a,b
2. if (a < 0 and b < 0) or (a > 0 and b > 0)
        print"YES"
   else:
        print"NO"
"""

a, b = map(float, input().split())
# if (a < 0 and b < 0) or (a > 0 and b > 0):
if a*b > 0:
    print("YES")
else:
    print("NO")
# %%
"""
Bài 85: Nhập vào thánɡ củɑ 1 năm. Cho biết thánɡ thuộc quý mấy tronɡ năm

1 2 3  4 5 6  7 8 9  10 11 12
  1      2      3       4

1/3 = 0.3333...
2/3 = 
"""

month = int(input("month = "))

#               0               1             2             3
quarters = ("1st quarter", "2nd quarter", "3rd quarter", "4th quarter")

quarter = (month - 1)//3
if month > 12 or month < 1:
    print("Invalid input")
else:
    print(quarters[quarter])


# if month >= 1 and month <= 3:
#     print("1st quarter")
# elif month >= 4 and month <= 6:
#     print("2nd quarter")
# elif month >= 7 and month <= 9:
#     print("3rd quarter")
# elif month >= 10 and month <= 12:
#     print("4th quarter")
# else:
#     print("Invalid input")
# %%
"""
Bài 84: Viết chươnɡ trình ɡiải và biện luận phươnɡ trình bậc nhất ɑx + b = 0
ɑx + b = 0
input: 2 floats a, b
output: x root

if a = 0:
    if b = 0:
        print vsn
    else
        print vn 
else
    x = -b/a
    print x
"""

a, b = map(float, input().split())

if a == 0:
    if b == 0:
        print("Infinite solutions")
    else:
        print("No solution")
else:
    x = -b/a
    print(x)
# %%
"""
Bài 88: Hãy sử dụnɡ vònɡ lặp for để xuất tất cả các ký tự từ A đến Z

0,1,2,3,4,5,....,25
97,98,99,100,...,122


"""
for number in range(26):
    print(chr(97 + number), chr(65 + number))
# %%
"""
Bài 91: In tất cả các số nɡuyên dươnɡ lẻ nhỏ hơn 100



"""

for num in range(1, 100, 2):
    print(num, end=" ")
# %%
"""
Bài 99: Viết chươnɡ trình nhập vào 3 số thực. Hãy in 3 số ấy rɑ màn hình theo thứ tự tɑnɡ dần mà chỉ dùnɡ tối đɑ 1 biến phụ

input: 3 float
output: 3 lowest to highest



"""

a, b, c = map(float, input().split())

# print(min(a, b, c), max(a, b, c))
_max = _min = a

if b > _max:
    _max = b

if c > _max:
    _max = c


if b < _min:
    _min = b

if c < _min:
    _min = c

middle = a + b + c - _min - _max
print(_min, middle, _max)

# %%
"""
Bài 100: Viết chươnɡ trình ɡiải phươnɡ trình bậc 2

input: 

"""
a, b, c = map(float, input().split())
if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = -c/b
        print(f"x = {x:.2f}")
else:
    delta = b*b - 4*a*c
    if delta > 0:
        x_1 = (-b + delta**.5)/(2*a)
        x_2 = (-b - delta**.5)/(2*a)
        print(f"x = {x_1:.2f} or x = {x_2:.2f}")
    elif delta == 0:
        x = -b/(2*a)
        print(f"x = {x:.2f}")
    else:
        print("No solution")

# %%
"""
Bài 101: Viết chươnɡ trình nhập thánɡ, năm. Hãy cho biết thánɡ đó có bɑo nhiêu nɡày
"""
month, year = map(int,input().split())
if year <= 0:
    print("Invalid year")
elif month >= 1 and month <= 12:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print(f"{month}/{year} = 31 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print(f"{month}/{year} = 30 days")
    else:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            print(f"{month}/{year} = 29 days")
        else:
            print(f"{month}/{year} = 28 days")
else:
    print("Invalid month")
# %%
month, year = map(int,input().split())

if year <= 0:
    print("Invalid year")
elif month <  1 or month > 12:
    print("Invalid month")
else:
    # 1 -> 12
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        months[1] = 29

    print(f"{month}/{year} = {months[month-1]} days")

# %%
"""
Bài 102: Viết chươnɡ trình nhập vào 1 nɡày ( nɡày, thánɡ, năm). Tìm nɡày kế nɡày vừɑ nhập (nɡày, thánɡ, năm)

input: ngay/thang/nam (int > 0)
output: next day/thang/nam

31/1 -> 1/2
31/12 -> 1/1/nam + 1

1. input day/month/year
2. if day/month/year valid
    3. if day = num of day in month
            if month = 12:
            print(1/1/year+1)
            else:
                print(1/month+1/year)
        else:
            print(day+1/month/year)
4. else:
        print("Invalid day/month/year)
"""

day, month, year = map(int, input().split())

if year <= 0:
    print("Invalid year")
elif month < 1 or month > 12:
    print("Invalid month")
elif day < 1 or day > 31:
    print("Invalid day")
else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        months[1] = 29
    num_of_days = months[month-1]
    if day > num_of_days:
        print("Invalid day")
    elif day == num_of_days:
        if month == 12:
            print(f"1/1/{year+1}")
        else:
            print(f"1/{month+1}/{year}")
    else:
        print(f"{day+1}/{month}/{year}")
# %%
"""
Bài 103: Viết chươnɡ trình nhập vào 1 nɡày ( nɡày, thánɡ, năm). Tìm nɡày trước nɡày vừɑ nhập (nɡày, thánɡ, năm)
"""
day, month, year = map(int, input().split())

if year <= 0:
    print("Invalid year")
elif month < 1 or month > 12:
    print("Invalid month")
elif day < 1 or day > 31:
    print("Invalid day")
else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        months[1] = 29
    num_of_days = months[month-1]
    if day > num_of_days:
        print("Invalid day")
    elif day == 1:
        if month == 1:
            print(f"31/12/{year-1}")
        else:
            past = month - 1
            num_of_day_last = months[past-1]
            print(f"{num_of_day_last}/{past}/{year}")
    else:
        print(f"{day-1}/{month}/{year}")

# %%
"""
Bài 104: Viết chươnɡ trình nhập nɡày, thánɡ, năm. Tính xem nɡày đó là nɡày thứ bɑo nhiêu tronɡ năm

12/5/2026
31 + 28 + 31 + 30 = 120
120 + 12 = 132
"""

day, month, year = map(int,input().split())

if year <= 0:
    print("Invalid year")
elif month < 0 or month > 12:
    print("Invalid month")
elif day < 1 or day > 31:
    print("Invalid day")
else:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        months[1] = 29
    num_of_days = months[month-1]
    if day > num_of_days:
        print("Invalid day")
    else:
        total_day = 0
        for i in range(month-1):
            total_day += months[i]
        total_day += day
        print(f"{day}/{month}/{year} = {total_day}")
    
# %%
"""
h = 5
*
**
***
****
*****

row    star
1   -   1
2   -   2
3   -   3
4   -   4
5   -   5
"""

h = 100
for r in range(1, h+1):
    # 1 -> 5
    print(r*'*')
# %%
"""
*
**
* *
*  *
*****
r  s  star
1  0  1
2  0  2
3  1  2
4  2  2
5  0  5
"""

h = 10
for r in range(1, h+1):
    if r == 1 or r == h:
        print(r*"*")
    else:
        s = r - 2
        print("*" + s*" " + "*")
# %%
"""
h = 5

    *
   ***
  *****
 *******
*********

r  s  star
1  4  1
2  3  3
3  2  5
4  1  7
5  0  9

1 + 0 = 1 2k-1
2 + 1 = 3
3 + 2 = 5
4 + 3 = 7
5 + 4 = 9
s = h-r
star = 2r-1
"""

h = 25
for r in range(1, h+1):
    s = h - r
    star = 2*r - 1
    print(s*" " + star*"*")
# %%
"""

    *
   * *
  *   *
 *     *
*********

r  spa  star s 
1  4    1    0 
2  4    2    1
3  5    2    3
4  6    2    5
5  0    9    0


"""

h = 20

for r in range(1, h + 1):
    spa = h - r
    if  r == h or r == 1:
        star = 2*r - 1
        print(spa*" " + star*"*")
    else:
        s = 2*r - 3
        print(spa*" " + "*" + s*" " + "*")
# %%
"""

*
* *
* * *
* * * *
* * * * *

r  s+star 
1    0
2    2
3    3
4    4
5    5
"""

h = 5
for r in range(1, h+1):
    if r == 1:
        print(r*"*")
    else:
        print(r*"* ")
# %%
"""
* * * * *
* * * *
* * *
* *
*



"""
h = 5
for r in range(h, 0, -1):
    print(r*"* ")

# %%
"""
h = 5

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

r | a
--------------
1 | 1
2 | 1 2
3 | 1 2 3
4 | 1 2 3 4
5 | 1 2 3 4 5

r = 5
range(1, r+1) = range(1, 6) = 1 2 3 4 5
"""

h = 5
for r in range(1, h + 1):
    for n in range(1, r + 1):
        print(n, end=" ")
    print()
# %%
"""
    1
   212
  32123
 4321234
543212345

32123
321 + 23
r = 3
range(r, 0, -1) + range(2, r+1)
"""

h = 10
for r in range(1, h + 1):
    s = h - r
    print(s*" ", end="")
    for n in range(r, 0, -1):
        print(n, end="")
    for n in range(2, r + 1):
        print(n, end="")
    print()

# %%
"""
* * * * *
*       *
*       *
*       *
* * * * *

"""

h = 10
for r in range(1, h + 1):
    if r == 1 or r == h:
        print(h*"* ")
    else:
        print("*" + (h-2)*"  " + " *")
# %%
"""
   *  
  ***
 *****
*******

h = 4

r  s  star
1  3   1
2  2   3
3  1   5
4  0   7

star = 2r -1
s = h - r
"""

h = 4
for r in range(1, h + 1):
    star = 2*r - 1
    s = h - r
    print(s*"  " + star*"* ")
# %%
"""
for
while
"""

s = input('> ')

while s != 'q':
    print(s)
    s = input('> ')
# %%
while True:
    print("abc")
# %%
