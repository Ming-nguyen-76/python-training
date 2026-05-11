#%%
from pprint import pprint

with open("iris.csv") as iris:
    doc = iris.readlines()
header = doc[0].strip().split(",")

irises = []
for row in doc[1:]:
    data = row.strip().split(",")
    nums = list(map(float, data[:-1]))
    values = nums + [data[-1]]
    irise_dict = dict(zip(header, values))
    irises.append(irise_dict)
pprint(irises)

with open("acb.csv", "w") as new_file:
    new_file.write(doc[0])
    for ch in irises:
        kien = ", ".join(map(str, ch.values()))
        new_file.write(kien + "\n")

# pprint(doc)
# %%
