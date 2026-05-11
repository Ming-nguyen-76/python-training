a = open(r"C:\Users\PC\OneDrive\Pictures\transportation.jpg") # raw
trietly = open("alphabet.txt", encoding="utf-8")
# c = trietly.readlines()

for line in trietly:
    print(line.strip())
trietly.close()
