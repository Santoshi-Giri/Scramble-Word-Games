import random 
from random import shuffle

inputfile = open("wordList.txt", "r")

file = inputfile.readlines()

wordList = []

for i in range(len(file)) :
     a = file[i].strip("\n")
     wordList.append(a)



randomNum = random.randint(0, len(wordList))
randomWord = wordList[randomNum]
print (randomWord)
 

Llist = []
for b in randomWord:
     Llist.append(b)
     
print (Llist)
shuffle(Llist)
Llist=''.join(Llist)
Llist=Llist.upper()
print(Llist)


print ("Welcome to CRYPTO-LOGIC!\nTry to guess the scrambled word, one letter at a time!")



gameend = False
incorrect=0
pletter = ''
i=0



while(gameend==False):
    print ("\nScrambled word: ", Llist)
    predictedletter = str(input("Enter your guess.."))
  
    if(predictedletter == randomWord[i]):
        
        i=i+1
        
        pletter += predictedletter
        
        print("Incorrect guess:",incorrect)
        print("Letters already guessed:",pletter.upper())

    else:
        incorrect+=1
        print("Incorrect guess:",incorrect)
        print("Letters already guessed:",pletter.upper())
    
    if(len(pletter)==len(randomWord)):
      
        gameend = True


print("Congratulations! You found the word after",incorrect,"incorrect guesses.")
    


x = input('')    
    
