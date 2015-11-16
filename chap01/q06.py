def char_ngram(text, n):
    results = []
    for i in range(len(text)-n+1):
        results.append(text[i:i+n])
    return set(results)

def word_ngram(text, n):
    results = []
    list = text.split()
    return char_ngram(list, n)

x = char_ngram("paraparaparadise", 2)
y = char_ngram("paragraph", 2)

print("X:")
print(x)
print("Y:")
print(y)
print("和集合:")
print(x & y)
print("差集合:")
print(x - y)
print("積集合:")
print(x | y)
print("se:")
print(bool(x & set(["se"])))
print(bool(y & set(["se"])))
