import os
import sys

f = open("hightemp.txt", "r")
list = f.readlines()
f.close()

n = int(sys.argv[1])
m = 0

for i in range(int(len(list)/n) + 1):
    result = ""
    f = open("out" + str(i) + ".txt", "w")
    for j in range(n):
        result += list.pop()
        if len(list) == 0: break
    f.writelines(result)
    f.close()
