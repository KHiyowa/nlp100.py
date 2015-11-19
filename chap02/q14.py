import os
import sys

n = int(sys.argv[1])
f = open("hightemp.txt", "r")
result = ""

for i in range(n):
    result += f.readline()

print(result)
f.close()
