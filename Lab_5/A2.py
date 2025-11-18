import re 

text = 'He jests at scars. That never felt a wound! Hello, friend! Are you OK?' 
sentences = re.split(r'(?<=[.?!]) ', text) 
count = 0 
for sentence in sentences:
    print(sentence, end='\n')
for sentence in sentences:
    if sentence in text:
        count += 1

print(f'Предложений в тексте: {count}')

