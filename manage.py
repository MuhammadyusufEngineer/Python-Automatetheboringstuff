# age = input()
# print('Ich bin ' + str(int(age) + 1) + ' jahre alt noch ein Jahr')

# name = ''
# while name != 'Myu':
#   print('Iltimos haqiqiy ismingizni yozing!')
#   name = input()
# print('Danke schone')
# import random

# for i in range(5):
#   print(random.randint(0,10))

import sys

# while True:
#   print('Type to exit')
#   response = input()
#   if response == 'exit':
#     sys.exit()
#   print('You typed ' + response + '.')

# import random

# secretNum = random.randint(0, 20)
# print("I'm thinking number between 0 and 20")

# for guessTaken in range(0, 6):
#   print('Take a guess')
#   guess = int(input())

#   if(guess < secretNum): print('your guess lower than my number')
#   elif(guess > secretNum): print('your guess is higher than my number')
#   else: break
# if(guess == secretNum): print('Correct, you found my number in ' + str(guessTaken) + ' times')
# else: print('Nope, the number I was thinking: ' + str(secretNum))

# import random, sys

# print('Rock, paper, scissors')

# wins = 0
# losses = 0
# ties = 0

# while True:
#   print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#   while True:
#     print('Enter your move: (r)ock (p)aper (s)cissor or (q)uit')
#     playerMove = input()
#     if playerMove == 'q':
#       sys.exit()
#     if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
#       break
#     print('Type one of r, p, s or q')

#   if playerMove == 'r':
#     print('Rock versus ...')
#   elif playerMove == 's':
#     print('Scissor versus ...')
#   elif playerMove == 'p':
#     print('Paper versus ...')

#   randomNumber = random.randint(1, 3)
#   if randomNumber == 1:
#     computerMove = 'r'
#     print('Rock')
#   elif randomNumber == 2:
#     computerMove = 'p'
#     print('Paper')
#   elif randomNumber == 3:
#     computerMove = 's'
#     print('Scissors')

#   if playerMove == computerMove:
#     print('It was a tie')
#     ties += 1
#   elif playerMove == 'r' and computerMove == 's':
#     print('You win')
#     wins += 1
#   elif playerMove == 'r' and computerMove == 'p':
#     print('You lose')
#     losses += 1
#   elif playerMove == 'p' and computerMove == 'r':
#     print('You win')
#     wins += 1
#   elif playerMove == 'p' and computerMove == 's':
#     print('You lose')
#     losses += 1
#   elif playerMove == 's' and computerMove == 'r':
#     print('You lose')
#     losses += 1
#   elif playerMove == 's' and computerMove == 'p':
#     print('You Win')
#     wins += 1

# import time, sys
# indent = 0
# indentIncreasing = True

# try:
#   while True:
#     print(' ' * indent, end='')
#     print('**Hallo**')
#     time.sleep(0.05) # pause for1/10 of a second
#     if indentIncreasing:
#       indent += 1
#       if indent == 20:
#         indentIncreasing = False
#     else:
#       indent -= 1
#       if indent == 0:
#         indentIncreasing = True

# except KeyboardInterrupt:
#   sys.exit()

# def collatz(number):
#     if number % 2 == 0:
#       return number // 2
#     else: return 3 * number + 1

# n = int(input('Enter a number: '))

# while n != 1:
#    n = collatz(n)
#    print(n)

# Slice method----------------------------------------------------------------------
# animals = ['bat', 'cat', 'rat', 'chat']
# new_cage = animals[1:2]
# print(new_cage)


# currentAnimals = ['lion', 'wolf', 'Camel']
# newAnimals = ['Koala', 'sloth', 'rabbit']
# zoo = currentAnimals + newAnimals

# print(zoo)


# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
#   print('Enter a name: (blank to quit)')
#   name = input()
#   if name == '' : break
#   if name in birthdays:
#     print(birthdays[name] + ' is the birthday of ' + name)
#   else:
#     print("I don't have birthday information for" + name)
#     print('What is the birthday?')
#     bday = input()
#     birthdays[name] = bday
#     print('Database update')


# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4214.')

# print(mo.group())
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())

# mo2 = heroRegex.search( )


# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile was lost')
# print(mo.group())

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The adventures of Batman')
# mo1 = batRegex.search('The adventures of Batwoman')
# mo1 = batRegex.search('The adventures of batman') # error
# print(mo1.group())

# phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())

# mo2 = phoneRegex.search('My number is 555-4242')
# print(mo2.group())

# Matching zero or more with * (asterisks)
# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The Adventures of Batman')
# mo2 = batRegex.search('The Adventures of Batwoman')
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo.group())
# print(mo2.group())
# print(mo3.group())

# Matching one or more with + (plus), it needs at least one, not optional
# batRegex = re.compile(r'Bat(wo)+man')
# mo2 = batRegex.search('The Adventures of Batwoman')
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())
# print(mo3.group())

# Greedy and non-greedy matching
### Python's regex is greedy by default, which means that it will match longest string possible,
# For example:
### greedyHaRegex = re.compile(r'(Ha){3,5}')
### mo1 = greedyHaRegex.search('HaHaHaHaHa')
# here it matches 5 which is maximum here
# and non-greedy would match first argument which is 3 in this example, and does not matches maximum 5

# and we use (?) for non-greedy match
# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# mo2.group()

# The findall() Method
# In addition to the search() method, Regex objects also have a findall() method. While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string. To see how search() returns a Match object only on the first instance of matching text, enter the following into the interactive shell:

# >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# >>> mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# >>> mo.group()
# '415-555-9999'

# On the other hand, findall() will not return a Match object but a list of strings—as long as there are no groups in the regular expression. Each string in the list is a piece of the searched text that matched the regular expression. Enter the following into the interactive shell:

# >>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# >>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']

# If there are groups in the regular expression, then findall() will return a list of tuples. Each tuple represents a found match, and its items are the matched strings for each group in the regex. To see findall() in action, enter the following into the interactive shell (notice that the regular expression being compiled now has groups in parentheses):

# >>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
# >>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# [('415', '555', '9999'), ('212', '555', '0000')]


# consonantRegex = re.compile(r'[aeiouAEIOU]')
# print(consonantRegex.findall('Robocop eats baby food. BABY FOOD'))

# ### (^) it is to make an exception
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print(consonantRegex.findall('Robocop eats baby food. BABY FOOD'))

# wholeStrIsNum = re.compile(r'^\d+$')
# print(wholeStrIsNum.search('1234567890')) # <re.Match object; span=(0, 10), match='1234567890'>
# print(wholeStrIsNum.search('12345xyz67890')) # None

# atRegex = re.compile(r'.at')
# print(atRegex.findall('That cat in the hat sat on the flat mat.'))

# nonGreedyRegex = re.compile(r'<.*?>')
# mo = nonGreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# GreedyRegex = re.compile(r'<.*>')
# mo = GreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# newLineregex = re.compile(r'.*')
# print(newLineregex.search('Serve the public trust.\nProtect the innocent.\nUpholad the law').group())
# newLineregex = re.compile(r'.*', re.DOTALL)
# print(newLineregex.search('Serve the public trust.\nProtect the innocent.\nUpholad the law').group())

# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENCORED', 'Agent Alice gave the secret documents to Agent Bob'))

# while True:
#   print('Enter your age')
#   age = input()
#   try:
#     age = int(age)
#   except:
#     print('Please use numeric digit')
#     continue
#   if age < 1:
#     print('Please use positive numbers')
#     continue
#   break
# print(f'Your age is {age}')

# from pathlib import Path
# print(Path('spam','bacon','egg'))
# import os
# print(Path.cwd())
# home = Path.home()

# os.makedirs(f'{home}/delicious')

import random
   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 
            'Alaska': 'Juneau', 
            'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 
   'California': 'Sacramento', 
   'Colorado': 'Denver',
   'Connecticut': 'Hartford', 
   'Delaware': 'Dover', 
   'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 
   'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# for quizNum in range(35):
#   quizFile = open(f'capitalzquiz{quizNum + 1}.txt', 'w')
#   answerKeyfile = open(f'capitalzquiz_answers{quizNum + 1}.txt', 'w')
#   quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
#   quizFile.write((" " * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
#   quizFile.write('\n\n')

#   states = list(capitals.keys())
#   random.shuffle(states)

# for questionNum in range(50):
#   correctAnswer = capitals[states[questionNum]] 
#   wrongAnswers = list(capitals.values())
#   del wrongAnswers[wrongAnswers.index(correctAnswer)]
#   wrongAnswers = random.sample(wrongAnswers, 3)
#   answerOptions = wrongAnswers + [correctAnswer]
#   random.shuffle(answerOptions)

#   quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

  
#   for i in range(4):
#     quizFile.write(f" {'ABCD'[i]}. {answerOptions[i]}\n")
#   quizFile.write('\n')

#   answerKeyfile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
  # quizFile.close()
  # answerKeyfile.close()

# for quizNum in range(35):
#   quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
#   answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w') 
#   quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n') 
#   quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})') 
#   quizFile.write('\n\n') 
#   states = list(capitals.keys())
#   random.shuffle(states)
#   for questionNum in range(50):
#     correctAnswer = capitals[states[questionNum]]
#     wrongAnswers = list(capitals.values())
#     del wrongAnswers[wrongAnswers.index(correctAnswer)]
#     wrongAnswers = random.sample(wrongAnswers, 3)
#     answerOptions = wrongAnswers + [correctAnswer]
#     random.shuffle(answerOptions)

#     quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
#     for i in range(4):
#       quizFile.write(f"    {'ABCD'[i]}. { answerOptions[i]}\n")
#       quizFile.write('\n')
#       answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
#   quizFile.close()
#   answerKeyFile.close()


### SAVE TO CLIPBOARD APPLICATION CLOSED
  #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

