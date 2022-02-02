import nltk
from nltk.tokenize import WhitespaceTokenizer
# pip install nltk
from collections import Counter
import random

print("If you have a text script, put the file is the current directory and enter its name including file extension.")
print("If you don't, just press 'Enter' and it will take the default file, it's a sample from Game of Thrones script.")
file_name = input("> ")
if file_name == "":
    file_name = "corpus.txt"

try:
    f = open(f"{file_name}", 'r', encoding="utf-8")
except FileNotFoundError:
    print("No such file or directory")
    quit()
f = f.read().split()
f = " ".join(f)

tokenizer = WhitespaceTokenizer()
tokens = tokenizer.tokenize(f)
trigrams = list(nltk.trigrams(tokens))

for sentence in range(10):
    while True:
        head = random.choice(trigrams)
        head = head[0:-1]
        if str(head[0]).isupper() is True and str(head[-1]) not in ".?!":
            break
    sentence = []
    sentence.append(head[0])
    sentence.append(head[1])
    while True:
        if len(sentence) < 5 and "." in " ".join(sentence):
            sentence = []
        if len(sentence) >= 5 and sentence[-1][-1] in ".!?":
            break
        else:
            freq_dict = {}
            for k in trigrams:
                if k[0:-1] == head:
                    headd = k[0]
                    freq_dict.setdefault(headd, []).append(k[-1])
            try:
                freq_counter = Counter(freq_dict[headd]).most_common()
            except KeyError:
                pass
            tail = freq_counter[0][0]
            sentence.append(tail)
            head = (head[-1], "".join(tail))
    print(" ".join(sentence))
