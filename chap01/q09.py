import random

def shuffle(text):
    list = text.replace(".", "").replace(":", "").split()
    align_t = []
    align_n = []
    shuffle = []

    for i in range(len(list)):
        if i == 0 or i == len(list)-1 or len(list[0]) <= 4:
            align_n.append(i)
            align_t.append(list.pop(0))
        else:
            shuffle.append(list.pop(0))

    random.shuffle(shuffle)

    for i in align_n:
        shuffle.insert(i, align_t.pop(0))
    return shuffle

print(shuffle(input()))

