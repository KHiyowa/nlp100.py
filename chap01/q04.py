from collections import Counter
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]

list = str.replace(",", "").replace(".", "").split()
for i in range(len(list)):
    list[i] = list[i][:2]
for i in one:
    list[i-1] = list[i-1][:1]

loc = range(1,21)
ans = dict(zip(list[:], loc[:]))

print(ans)
