import os

f = open("hightemp.txt", "r")
col1 = f.readline()
col2 = f.readline()
f.close()

f = open("col1.txt", "w")
f.write(col1)
f.close()

f = open("col2.txt", "w")
f.write(col2)
f.close()
