import random

def guessingNumber(b):
    randomNumber = random.randint(1 , b)
    guessingNumber = 0
    while guessingNumber != randomNumber :
      guessingNumber = int(input(f'guess a random number between 1 and {b} :-'))

      if guessingNumber < randomNumber :
            print('''sorry ! it's too low''')
      elif guessingNumber > randomNumber :
            print(''' sorry ! it's too high ''')
            
    print(f'congratulations ! you guessed a correct number : {guessingNumber}')       

    


guessingNumber(10)
