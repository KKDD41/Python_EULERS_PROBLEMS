F = open('c:/Users/Kate/Desktop/tests/problems/EULER/words.txt')
f = F.read()
words = list(f.replace(',', '').split('""'))


def anagram(word0, words):
    anagrams = {word0}
    for word1 in words:
        if all((len(word0) == len(word1) and word0.count(i) == word1.count(i) for i in word0)):
            anagrams.add(word1)
    return anagrams


pairs = []
for i in range(len(words)):
    if len(anagram(words[i], words)) > 1:
        pairs.append(anagram(words[i], words))
