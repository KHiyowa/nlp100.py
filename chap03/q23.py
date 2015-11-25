import re

result = []
patternf = "==*[^=]+=*=\n"
patternh = "=*"
patternt = "\n"

for datum in open("jawiki-uk.txt", "r").readlines():
    if re.search(patternf, datum) != None:
        num = int(datum.count("=") / 2) - 1
        datum = re.sub(patternh, "", datum)
        datum = re.sub(patternt, "", datum)
        result.append([datum, num])

print(result)
