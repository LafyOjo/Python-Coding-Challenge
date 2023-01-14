def reverse_words_punctuation(sentence):
    words = []
    word = ""
    for char in sentence:
        if char.isalnum() or char == " ":
            word += char
        else:
            words.append(word)
            word = ""
            words.append(char)
    words.append(word)
    words = words[::-1]
    return "".join(words)
