import re

result = []

f = open("jawiki-uk.txt", "r")
string = f.read()
f.close()

data = str(re.findall("{{基礎情報.+\n}}", string, re.DOTALL)).split(r"\n")

dic = {}

for datum in data:
    if re.search("\|.+=.+", datum) != None:
        tmpkey = re.sub("\|", "", datum)
        tmpkey = re.sub(" =.+", "", tmpkey)
        tmpvalue = re.sub(".+=", "", datum)
        tmpvalue = re.sub("\'\'+", "", tmpvalue)
        tmpvalue = re.sub("\[\[", "", tmpvalue)
        tmpvalue = re.sub("(\|[^\]]+)*\]\]", "", tmpvalue)
        dic[tmpkey] = tmpvalue

print(dic)
print(len(dic))
