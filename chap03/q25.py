import re

result = []

f = open("jawiki-uk.txt", "r")
string = f.read()
f.close()

data = str(re.findall("{{基礎情報.+\n}}", string, re.DOTALL)).split(r"\n")

dic = {}

for datum in data:
    tmpkey = re.sub("\|", "", datum)
    tmpkey = re.sub(" =.+", "", tmpkey)
    tmpvalue = re.sub(".+=", "", datum)
    dic[tmpkey] = tmpvalue

print(dic)
