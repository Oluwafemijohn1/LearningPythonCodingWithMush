from collections import Counter
from pprint import pprint
sentence = "This is a common interview question"
list_of_char = list(sentence)
# the most common character in the sentence


char_frequency = {}
for char in list_of_char:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

sorted = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
print("The most common character is: ",
      sorted[0][0], "with frequency: ", sorted[0][1])


def most_common_char(sentence):
    char_count = Counter(sentence)
    most_common = char_count.most_common(1)
    return most_common[0] if most_common else None
