import os

f = open("hightemp.txt", "r")
str = f.readlines()
f.close()

list = []

for i in range(len(str)):
    temp = str[i].split()
    list.append(temp[0])
print(set(list))
