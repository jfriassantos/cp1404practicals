"""
Word Occurrences:
Estimate: 30 minutes
Actual:   13 minutes
"""

word_to_count = {}
text = input("Text: ")
for word in text.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
width = max(len(word) for word in word_to_count)
for word in sorted(word_to_count):
    print(f"{word:{width}} : {word_to_count[word]}")
