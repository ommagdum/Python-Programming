# List of words
words = ["Om", "Magdum", "TY", "B.Tech", "Roll", "127", "Division", "B"]

# Using dictionary comprehension to calculate lengths
word_length_dict = {word: len(word) for word in words}

print("Dictionary of word lengths:")
for word, length in word_length_dict.items():
    print(f"'{word}': {length}")