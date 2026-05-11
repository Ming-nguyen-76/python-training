#%%
from pprint import pprint
iris = open("iris.csv")
doc = iris.readlines()
iris.close()
irises = []
for row in doc[1:]:
    sepal_length,sepal_width,petal_length,petal_width,species = row.strip().split(",")
    irises.append({
        "sepal_length" : float(sepal_length),
        "sepal_width" : float(sepal_width),
        "petal_length" : float(petal_length),
        "petal_width" : float(petal_width),
        "species" : species
    })
# pprint(irises)

new_file = open("acb.csv", "w")
new_file.write(doc[0])
for ch in irises:
    kien = ", ".join(map(str, ch.values()))
    new_file.write(kien + "\n")

new_file.close()
pprint(doc)
# %%
