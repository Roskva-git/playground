#Magic eightball program

#Generating a random integer between one and 9
import random
random_number = random.randint(1,10)

#On the website we will ask for the player's name. Remember to get an input field with html
#It will look something like this
#name = input("Enter your name: ")
#print(f"Hello, {name}!")

name = ('Røskva')
question = 'Will I be rich?'

#Action time
print(str(name) + ' asks: ' + str(question))
print('''\nMagic 8-ball's answer:''')


#Trying out the match case function nested within an if else

if question == '':
  print('''I didn't catch that.''')
else:
  match random_number:
    case 1:
      print('Yes - definitely')
    case 2:
      print('It is decidedly so')
    case 3:
      print('Without a doubt')
    case 4: 
      print('Reply hazy, try again')
    case 5: 
      print('Ask again later')
    case 6:
      print('Better not tell you now')
    case 7:
      print('My sources say no')
    case 8:
      print('Outlook not so good')
    case 9: 
      print('Very doubtful')
    case _:
      print("ERROR! I don't know what we're doing here.") 
