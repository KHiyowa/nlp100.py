import os

f = open("hightemp.txt", "r")
data = f.readlines()
f.close()

result = {}

for i in range(len(data)):
    tmp = data[i].split("\t")
    try:
        result[tmp[2]].append(data[i])
    except:
        result[tmp[2]] = []
        result[tmp[2]].append(data[i])

index = sorted(result.keys())
for i in index[::-1]:
    tmp = result[i]
    while ( len(tmp) != 0 ):
        print(tmp.pop(), end="")

