def char_ngram(text, n):
    results = []
    for i in range(len(text)-n+1):
        results.append(text[i:i+n])
    return results

def word_ngram(text, n):
    results = []
    list = text.split()
    return char_ngram(list, n)

str = "I am an NLPer"
print(word_ngram(str, 2))
print(char_ngram(str, 2))
