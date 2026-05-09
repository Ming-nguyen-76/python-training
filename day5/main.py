# %%
import string
print(bool("Hi"))

# %%
age = 27

if age > 18:
    print("beer")
if age > 10:
    print("milk")
else:
    print("coca")

# %%
a, b, c = 100, 1000, 333

if a < b and a < c:
    print(a, "is the smallest")
elif b < a and b < c:
    print(b, "is the smallest")
else:
    print(c, "is the smallest")

if a > b and a > c:
    print(a, "is the largest")
elif b > a and b > c:
    print(b, "is the largest")
else:
    print(c, "is the largest")
# %%
a, b, c = 1.0, 1000.0, 3333.0

_max = _min = a

if b > _max:
    _max = b

if c > _max:
    _max = c

if b < _min:
    _min = b

if c < _min:
    _min = c

print(_max, _min)
# %%
a, b, c = 1.5, 100.5, 33.33
print(max(a, b, c))
print(min(a, b, c))

# %%
print(string.ascii_lowercase)
# %%
"""
01234567890123456789012345
abcdefghijklmnopqrstuvwxyz
"""

# %%
n = 1
if n % 2 == 0:
    print("even")
else:
    print("odd")

# %%
year = 2000
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap year")
else:
    print("normal year")

# %%
name = input("Please enter your name: ").strip()

if name:  # Checks the truth value of name by calling bool
    print(f"You entered {name}")
else:
    print("You didn't type anything")

# %%
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

b = a.copy()
print(a == b)
print(a is b)

# %%
list
numbers = [1, 2, 3, 4]
print(id(numbers))
# numbers = numbers + [5]
numbers += [5]
print(id(numbers))

numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))
# %%
num = float(input("Enter a number: "))
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else:
    print("negative number")
# %%
hours_worked = float(input("How much hours you worked this week? "))
hourly_wage = float(input("What is your hourly wage? "))

if hours_worked > 40:
    additional_pay = (hours_worked - 40)*hourly_wage*1.1
    total_earning = 40*hourly_wage + additional_pay
    print(f"Your additional pay is ${additional_pay}")
    print(f"Total earning: ${total_earning}")
else:
    total_earning = hours_worked*hourly_wage
    print(f"Total earning: ${total_earning}")
# %%
hours_worked = float(input("How much hours you worked this week? "))
hourly_wage = float(input("What is your hourly wage? "))

total_earning = hours_worked*hourly_wage


if hours_worked > 40:
    additional_pay = (hours_worked - 40)*hourly_wage*1.1
    total_earning = 40*hourly_wage + additional_pay
    print(f"Your additional pay is ${additional_pay}")

print(f"Total earning: ${total_earning}")
#%%
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))
print(a is a)

#%%
# >, <, >=, <=, ==, !=
# => True/False
1 > 2

3 > 2 > 1

3 > 2 > 100

'a' > 'b'

print(ord('a'))
print(ord('b'))
print('A' > 'b')

print(ord('A'))
'a' > 1
'a' == 1
#False

'a' != 1
#True

5 + 4 < 3 * 2
#False

5 + (4 < 3) * 2
#5

# not > and > or
# and
True and True
#True
True and False
#False
False and False
#False
False and True
#False
1 > 2 and 3 > 4
#False
4 > 2 and 'a' > 'A'
#True
print(ord('z'))
#122

# or
True or True
#True
True or False
#True
False or False
#False
False or True
#True
print(1 > 2 or ' ' > '')
#True

not True
#False
not False
#True
print(not 1 > 2 or 3 > 100 and 'a' > 'B')
#True

bool(1)
#True
bool(2)
#True
bool(.0)
#False
print(0.0 == 0)
True
bool([])
#False
bool([1])
#True
bool((1,))
#True
bool(())
#False
bool('')
#False
bool(' ')
#True
bool(None)
#False

1 and 2
#2

0 and 2
#0
[] and 3
#[]
'' and None
#''
1 or 2
#1
0 or 2
#2
'' or 'Ming'
#'Ming'
None or 1j
#1j
not 1
#False
not 0
#True
print(not 1 or 2 and 3)
#3
n = 3
n % 2

# %%
a = float(input())
b = float(input())
c = float(input())
print(max(a, b, c))
print(min(a, b, c))
# %%
