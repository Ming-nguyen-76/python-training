from pprint import pprint

phone = {
    "0123456789" : "Ming",
    "0999999999" : "Kien",
    "1800018800" : "Duy",
    "0123456123" : "Xanh",
    "0987654321" : "Huy",
    "0888888888" : "Khanh",
    "0777777777" : "Vy",
    "0666666666" : "Minh Anh",
    "0555555555" : "Lady Boy",
    "0333333333" : "Quan"
}

print(phone["1800018800"])
phone["1800018800"] = "Dat"
print(phone["1800018800"])
for key, value in phone.items():
    print(f"{key} : {value}")
del phone["1800018800"]
pprint(phone)
phone["0111119999"] = "Jay"
pprint(phone)
new_phone = {
    "0222222222" : "Lan",
    "0666667777" : "Chau",
    "0838683866" : "Linh"
}

phone.update(new_phone)
pprint(phone)

phone.pop("0838683866")
pprint(phone)