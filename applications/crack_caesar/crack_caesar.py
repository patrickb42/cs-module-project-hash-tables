# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DECODED_LETTERS_BY_FREQUENCY = 'ETAOHNRISDLWUGFBMYCPKVQJXZ'
frequency = {key: 0 for key in LETTERS}

with open('ciphertext.txt') as cipher_text_file:
    for line in cipher_text_file:
        for char in line:
            if char in frequency:
                frequency[char] = frequency[char] + 1

letters_by_frequency = sorted(frequency, key=frequency.get, reverse=True)
print(letters_by_frequency)
CIPHER_DECODE_TABLE = {
    key: DECODED_LETTERS_BY_FREQUENCY[index]
    for (index, key) in enumerate(letters_by_frequency)
    if key in frequency
}

with open('ciphertext.txt') as cipher_text_file:
    for line in cipher_text_file:
        decoded_line_arr = []
        for char in line:
            decoded_char = CIPHER_DECODE_TABLE[char] if char in frequency else char
            decoded_line_arr.append(decoded_char)
        print("".join(decoded_line_arr))
