import spacy
from collections import Counter

# Loads English language model
nlp = spacy.load("en_core_web_sm")

# Defines a Counter to store word frequencies
word_freq = Counter()

# Processes text from a file line by line
with open("random_paragraphs.txt", "r") as file:
    for line in file:
        # Processes each line with spaCy
        doc = nlp(line)

        # Removes stop words and punctuation, and count word frequencies
        for token in doc:
            if not token.is_stop and not token.is_punct:
                word_freq[token.text.lower()] += 1

# Displays word frequency count
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
