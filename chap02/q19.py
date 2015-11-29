import os

COLUMN = 0

f = open("hightemp.txt", "r")
data = sorted(f.readlines())
f.close()

relation = {}

for i in data:
    tmp = i.split("\t")
    key = tmp[COLUMN]
    try:
        relation[key] = relation[key] + 1
    except:
        relation[key] = 1

index = sorted(relation.items(), key=lambda x:x[1])

for k, v in index[::-1]:
    for i in data:
        tmp = i.split("\t")
        if k == tmp[COLUMN]:
            print(i, end="")
