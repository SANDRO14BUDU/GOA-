def insert_word(sentence, word, index):
    words = sentence.split()
    if 0 <= index <= len(words):
        words.insert(index, word)
        return ' '.join(words)
    return "Invalid index."

sentence = "I love programming challenges."
word = "really"
index = 2
result = insert_word(sentence, word, index)
print(result)
