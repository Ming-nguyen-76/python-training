# %%
from pprint import pprint
a = 2


def add():
    global a
    a = 5
    a += 5


add()
print(a)
globals()['add']()
print(a)
# %%
def add(a, b, c):
    a = 10
    x = 100
    print(locals())
    print(a + b + c)


add(1, 3, 5)

# %%
