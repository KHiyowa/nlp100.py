import json
import os

w = open("jawiki-uk.txt", "w")

for data in open("jawiki-country.json", "r"):
    datum = json.loads(data, "utf-8")
    if datum["title"] == "イギリス":
        result = datum["text"]
        w.write(result + "\n")

