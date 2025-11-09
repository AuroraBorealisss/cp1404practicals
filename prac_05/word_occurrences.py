"""
CP1404/CP5632 Practical
Program to count occurrences of words in a string
estimate: 20 mins
actual: 11.5 mins (base task, no sorting/align)
actual: 53.5 :c
"""
word_to_count = {}
text_sample = input("Text: ").lower()
column_width = 0
words = text_sample.split(' ')
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
column_width = max(len(word) for word in words)
for word in sorted(word_to_count):
    print(f"{word:{column_width}} : {word_to_count[word]}")
