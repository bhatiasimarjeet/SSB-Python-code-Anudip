def count_word_occurrences(sentence):
    word_count = {}
    word = ""
    words = []
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check for space or punctuation to separate words
        if char == ' ' or char in ",.!?:;'":
            if word != "":
                words.append(word.lower())
                word = ""
        else:
            word += char
    
    # Account for the last word in the sentence
    if word:
        words.append(word.lower())
    
    # Count occurrences of each word
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    
    return word_count

# Example usage
input_sentence = "This is a sample sentence. This sentence is a sample."
word_occurrences = count_word_occurrences(input_sentence)

# Display word occurrences
for word, count in word_occurrences.items():
    print(f'Word "{word}" occurs {count} time(s)')