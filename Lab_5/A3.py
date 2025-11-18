text = input('Ведите текст: ')
words = text.split()
for word in words:
    if len(word) >= 3:
        first_letter = word[0].upper()
        print(first_letter, end='')