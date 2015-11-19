import os
import sys

f = open("hightemp.txt", "r")
list = f.readlines()
f.close()

n = len(list) - int(sys.argv[1])

while n < len(list):
    print(str(list[n]), end="")
    n += 1
