#text = 'Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).'
#while '(' and ')' in text:
#    left = text.rfind('(')
 #   right = text.find(')', left)
  #  if right != -1:
   #     text = text[:left] + text[right+1:]
#text = text.replace(' ', ' ').strip()
#text = text.replace(' .', '.').replace('?', '?').replace(',', ',').replace('!', '!')
    #text = text.replace(text[left:right+1], '')
#print(text)

text = 'Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).'

while '(' in text and ')' in text:
    left = text.rfind('(')
    right = text.find(')', left)

    if right != -1:
        if left > 0 and text[left - 1] == ' ':
            text = text[:left - 1] + text[right + 1:]
        else:
            text = text[:left] + text[right + 1:]

text = ' '.join(text.split())
#text = text.replace(' .', '.').replace(' ,', ',').replace(' !', '!').replace(' ?', '?')

print(text)