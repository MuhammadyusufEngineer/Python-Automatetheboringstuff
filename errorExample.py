# def spam():
#   bacon()

# def bacon():
#   raise Exception('This is an error message')

# spam()

# import traceback
# try:
#   raise Exception('This is the error message.')
# except:
#   errorFile = open('ErroInfo.txt', 'w')
#   errorFile.write(traceback.format_exc())
#   errorFile.close()
#   print('The tracebackinfo was written into errorinfo.txt')

# ages = [26, 243 ,65,123,76,3,5, 4]
# ages.sort()
# print(ages)

# assert ages[0] <= ages[-1]

# spam = 1
# assert spam > 10, "spam is less than 10"


#### XATO, ishlamayapti
# beef = 'ghalo'
# lamb = 'hello'

# assert beef == lamb, "Both contains same string"

# import random, logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# logging.debug('Start of program')
# condition = ['heads', 'tails']
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
#     logging.debug('First guess: ' + guess)
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
# logging.debug(f'toss: {toss}')
# if condition[toss] == guess:
#     logging.debug(f'first correct toss and guess: {guess} {toss} {condition[toss]}')
#     print('You got it!')
# else:
#     logging.debug(f'first time wrong guess: {guess}, toss: {toss} {condition[toss]}')
#     print('Nope! Guess again!')
#     guess = input()
#     if condition[toss] == guess:
#         print('You got it!')
#         logging.debug(f'second time guess: {guess}, toss: {toss} {condition[toss]}')
#     else:
#         print('Nope. You are really bad at this game.')
# logging.debug('End of a program')