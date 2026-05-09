#%%
print("a" + "b")

# %%
print("1" + 1)

# %%
print(int("18.5"))

# %%
print(int(18.5))

# %%
age = 17
# I am 17
print("I am ", age)
print("I am {}".format(age))
print(f"I am {age}")

# %%
s = " hello world    "
print(len(s))
s = s.lstrip()
print(len(s))

print(s.strip())
# %%
greeting = "Hello World"
print(f"{greeting}!")
print(greeting + "!")
greeting = "Hello World{}"
print(greeting.format("!"))
# %%
name = input("What is your name? ")
new_name = name.strip()
new_name = new_name.title()
greeting = "Hello {}!"
print(greeting.format(name))
print(f"Hello {name}!")
# %%
age = 29
print("I am " + str(age))
print("I am {}".format(age))
print(f"I am {age}")
# %%
title = "Joker"
director = "Todd Phillips"
release_year = 2019
print("{} ({}), directed by {}".format(title, release_year, director))
print(f"{title} ({release_year}), directed by {director}")
# %%
name = input("What is your name? ").strip().title()

hourly_wage = float(input("What is your hourly wage? "))

hours_worked = float(input("How many hours you worked this week? "))

total_earning = hourly_wage*hours_worked
# total_earning = round(total_earning, 2)

print(f"{name} earned ${total_earning:.2f} this week.")
# %%
