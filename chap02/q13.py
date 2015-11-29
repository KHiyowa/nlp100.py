import os

f1 = open("col1.txt", "r")
f2 = open("col2.txt", "r")

fw = open("colmerge.txt", "w")
result = f1.read() + f2.read()
fw.write(result.replace("\n", "\t"))

f1.close()
f2.close()
fw.close()
