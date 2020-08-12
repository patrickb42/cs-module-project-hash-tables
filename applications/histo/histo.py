# Your code here
from functools import cmp_to_key
import time
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

blacklist = {
    '"',
    ':',
    ';',
    ',',
    '.',
    '-',
    '+',
    '=',
    '/',
    '\\',
    '|',
    '[',
    ']',
    '{',
    '}',
    '(',
    ')',
    '*',
    '^',
    '&',
}
frequency = {}
longest_word_len = 0

with open('robin.txt') as robin_file:
    for line in robin_file:
        words = line.split()
        for word in words:
            normalized_word_arr = []
            for char in word.lower():
                if char not in blacklist:
                    normalized_word_arr.append(char)
            normalized_word = ''.join(normalized_word_arr)
            longest_word_len = len(normalized_word)\
                if len(normalized_word) > longest_word_len else longest_word_len
            if normalized_word in frequency:
                frequency[normalized_word] += 1
            else:
                frequency[normalized_word] = 1

t0 = time.time()
def wrapper(target):
    def ranker(item1, item2):
        nonlocal target
        if target[item1] > target[item2]:
            return -1
        elif target[item1] < target[item2]:
            return 1
        elif item1 > item2:
            return 1
        elif item1 < item2:
            return -1
        else:
            return 0
    return ranker
COUNT = 50_000
for _ in range(COUNT):
    sorted(frequency, key=cmp_to_key(wrapper(frequency)))
print(time.time() - t0)
t1 = time.time()
for _ in range(COUNT):
    sorted(frequency, key=lambda key: (-frequency.get(key), key))
print(time.time() - t1)
t2 = time.time()
for _ in range(COUNT):
    sorted(sorted(frequency), key=frequency.get, reverse=True)
print(time.time() - t2)
# for key in sorted(frequency, key=cmp_to_key(wrapper(frequency))):
# for key in sorted(frequency, key=lambda key: (-frequency.get(key), key)):
    # print(f'{key} {" " * (longest_word_len - len(key))} {"#" * frequency[key]}')
