import re

result = []

f = open("jawiki-uk.txt", "r")
data = f.readlines()
f.close()

patternh = "\[\[Category:"
patternt = "(\|\*)*(\]\]\n)"

for datum in data:
    if datum.find("Category") >= 0:
        datum = re.sub(patternh, "", datum)
        datum = re.sub(patternt, "", datum)
        result.append(datum)



print(result)
