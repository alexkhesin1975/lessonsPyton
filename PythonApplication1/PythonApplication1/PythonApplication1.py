
f = open("test.txt", "r")

s = f.readline()
while s:
    print(s)
    s = f.readline()

f.close()