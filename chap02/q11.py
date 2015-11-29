import os

f = open("hightemp.txt", "r")
print(f.read().replace("\t", " "))
f.close()
