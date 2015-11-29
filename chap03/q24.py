import re

result = []
patternf = "(ファイル:).+\n"
patternh = ".*ファイル:"
patternt = "\|.*\n"

for datum in open("jawiki-uk.txt", "r").readlines():
    if re.search(patternf, datum) != None:
        datum = re.sub(patternh, "", datum)
        datum = re.sub(patternt, "", datum)
        result.append(datum)

print(result)
