print("welcome to the game of guessing the number")
print( " I am your host hammad")
Name = input("can i know your good name please:")


secretNumber = 21
guessNumber = 0

while secretNumber != guessNumber:
      guessNumber = int(input(Name  +   " please guess the number,give it your best shot: "))
      if (secretNumber < guessNumber):
        print("bit lower dumbnut ;D ")
      elif (secretNumber > guessNumber):
        print("bit higher genius")
      else:
          print("congratulations ")
          print(" As a reward you will be gifted a new client")
 
