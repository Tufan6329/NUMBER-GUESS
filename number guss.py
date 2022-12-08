import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0

while(userGuess !=randNumber):
      userGuess=int(input("plyer:enter your guess:"))
      guesses+=1
      if(userGuess==randNumber):
          print("you guessed is right!")
      
      else:
          if(userGuess>randNumber):
             print("you guessed is wrong ! enter a smpaller number!")
          else:
             print("you guesses it wrong! enter a larger number")
          
print(f"guess the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
     
      hiscore=int(f.read())

if(guesses<hiscore):
    print("you have just broken the high score!")
    with open("hiscore.txt","w") as f:
         f.write(str(guesses))