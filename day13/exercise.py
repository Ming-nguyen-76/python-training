#%%
def exponentiate(base, power):
    return base**power


print(exponentiate(4,3))
# %%
def process_string(s):
    return s.lower().strip()


print(process_string("AKIEN"))
# %%
def identify(user_info):
    name, nationality, age = user_info
    return {
        "name" : name,
        "nationality" : nationality,
        "age" : age
    }


print(identify(("Ming", "Chinese", 18)))
# %%
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**.5) + 1):
        if n%i == 0:
            return False
    return True

print(is_prime(100))
# %%
