import random

lucky_number = random.randint(1,100)

fortune_number = random.randint (1,3)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'Everything you wish for you shall recieve'
if fortune_number == 2:
  fortune_text = 'Smile you never know who needs it.'
if fortune_number == 3:
  fortune_text = 'Buy two scratch offs you might just win.. one of these days'
if fortune_number == 4:
  fortune_text = 'Shoot your shot. YOLO. They might just be the love of your life.. but use your best pick-up line.'
if fortune_number == 5:
  fortune_text = 'If you stay ready, you dont have to get ready'

print(f'{fortune_text} Your Lucky Number is: {lucky_number}')