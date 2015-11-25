import re

result = []

f = open("jawiki-uk.txt", "r")
data = f.readlines()
f.close()

for datum in data:
    if datum.find("Category") >= 0:
        result.append(datum)

print(result)
