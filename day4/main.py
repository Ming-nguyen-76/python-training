# # list
# # %%
# x = 5
# a = [1, 2, 3]
# a = [1, 1.5, True, "abc"]
# print(a)

# friends = ["Minh", "Vy", "Ngoc", "Xanh", "Nam", "Khanh", "Huy", "Nhi", "Vanh", "Uyen"]

# print(type(friends))

# %%
#             0      1     2       3        4       5       6      7      8       9
friends = ["Minh", "Vy", "Ngoc", "Xanh", "Nam", "Khanh", "Huy", "Nhi", "Vanh", "Uyen"]

print(friends)
friends.append("Hung")
friends.extend(["Manh", "Trang", "Vu"])
friends.insert(1, "Linh")

print(len(friends))
print(friends[3])
print(friends[-1])
print(friends[-3])
n = len(friends)
print(friends[n-1])
print(friends[-n])

"""
list
index: 0 -> len-1 (positive)
    -len -> -1    (negative)
"""
friends.insert(0, "Vu")
print(friends)
friends.remove("Vu")
# friends.pop(100)
print(friends)

del friends[0]

print(friends)

print(friends.count("VU"))
friends.sort()
print(friends)

friends.reverse()

print(friends)

numbers = [1, 5, 3, 2000, 345, 67785, 234, 444, 333, 777, 2000, 1, 1, 5, 7, 444]

numbers.reverse()

print(numbers.copy())

print([1, 2, 3] + [3, 4])

numbers.clear()

print(numbers)

# %%
#       0  1  2   3    index
nums = (1, 4, 3, 45) # value
print(nums)
nums = nums + (1, 2, 3)
print(nums)
print(nums[1])
# %%
movies = [
    ("Supernam", 2020),
    ("Spiderman", 2019),
    ("Ironman", 2021)
]

print(movies[2][1])
print(movies[1][0])
movies.append(("Batman", 2018))
print(movies)
# %%
# 1.
movies = [("Avatar: The Way Of Water", "Disney", 2022, 350)]
# 2.
title = input("What is the title of the movie? ")
director = input("What is the name of the director? ")
release_year = int(input("What year was the movie released? "))
budget = float(input("What is the budget of the movie? "))
# 3.
movie = (title, director, release_year, budget)
# 4.
print(f"{title}, {release_year}")
# 5.
movies.append(movie)
# 6.
print(movies[0])
print(movies[1])
# 7.
"""
1. remove - value
2. pop - index and return value
3. del - index
"""
del movies[0]
print(movies)
# %%
#    0   1   2   index
a = [1, 100, 3]
#   [1, 3, 100]
#a[1] = 2
# b = a[1]
# a[1] = a[2]
# a[2] = b
a[1], a[2] = a[2], a[1]
print(a)
# %%
