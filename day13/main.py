#%%
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
