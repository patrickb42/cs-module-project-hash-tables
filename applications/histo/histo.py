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

for key in sorted(sorted(frequency), key=frequency.get, reverse=True):
    print(f'{key} {" " * (longest_word_len - len(key))} {"#" * frequency[key]}')
