from collections import Counter

file_1 = "aaa.pfile_1  lalalalalala lll23flf; 23'' dd/ dwd32wd[] dwdwdwd{2323@} : dwddwdd"
file_2 = "аа lll23flf; 23'' dd/ dwd32wd[]"

ffg = open('aaa.py')
points = ffg.read().splitlines()
ffg.close()
print(ffg)

def hhd(file, num):
    b = ""
    num = 5
    for i in file:
        if i.isalnum():
            b += i
        elif b[len(b) - 1] != " " and i != len(file) - 1:
            b += " "

    ar = []
    c = ""
    for f in b:
        if f.isalnum():
            c += str(f)
        elif f == " ":
            ar.append(c)
            c = ""
    ar.append(c)
    return ar


ar1 = hhd(file_1, 1)
ar2 = hhd(file_2, 1)

x = Counter(ar1)
y = Counter(ar2)
print(x)
print(y)

if x == y:
    print("HU")

t = 0
for keyx in x:
    for keyy in y:
        if keyx == keyy:
            if x[keyx] <= y[keyy]:
                t += x[keyx] / y[keyy]
            if x[keyx] > y[keyy]:
                t += y[keyy] / x[keyx]
q = 0
if len(x) < len(y):
    q = len(y)
else:
    q = len(x)

print(t / q)