# Scramble-Word-Games

## Summary of the Program 

This is a program which is written to play scrambled word game. In this game, the letters of a randomly selected dictionary word are scrambled and the players has to guess the word, letter by letter. It also displays the number of incorrect guess made by the player and also the output after how many guess the player was able to guess the word. 

## Downloading and installing Python:

**1.** First download the python by visiting python.org/downloads and choose the latest version to download.

**2.** After the python is downloaded , double click on the executable downloaded software and run it.

**3.** A pop up window with python version setup will appear. Click on the check boxes and click "yes".

**4.** Now you can install the python by clicking on install.

## Steps for running the program:

**Step 1:** Go to the start menu and search for Python IDLE and open it.

**Step 2:** Click on the file then go to New File where you will e able to write your code.

**Step 3:** Make sure to save your code before running them. After saving you can compile and run your code by simply pressing F5 in the keyboard or choosing from the "Run" botton which is on the top of the python shell.

## Description of the Scramble-Word-Game
The program reads the list of words from the attached file named "wordList.txt" one at a time and adding each word to the list. This file consist of 300 random dictionary words. Among them 100 are six letter long, 100 are seven letter and remaining 100 are more eight or more than that. A secret word is chosen from the wordlist, break them into list of individual letters and then create a scramble copy of the list. This program first display the list of scramble words, printed scramble word and welcome the user with instruction to play the game. The player is allowed to guess only one word at a time. After guessing each word, it shows whether the guess was right or wrong along with the printed scrambled word with the number of incorrect guess and any correct letter player has guessed. Again, the player is prompt to guess the letter and compared with the next letter of the secret word. If the guess does not matches, the number of incorrect guess increases by one and if the guessed word is correct then it adds the letter to the list of correctly guessed. This process keep on repeating until all the letters matches as well as become equal to the length of the secret word. At that point, the game is over by displaying the completed word along with the a message of total incorrect guesses the player made.

## The output of the game looks like:

    Welcome to Scramble - Word-Game!

    Try to guess the scrambled word, one letter at a time!

    Scrambled word:  NNOWRDU
    Enter your guess..w
    Incorrect guess: 1
    Letters already guessed: 

    Scrambled word:  NNOWRDU
    Enter your guess..o
    Incorrect guess: 2
    Letters already guessed: 

    Scrambled word:  NNOWRDU
    Enter your guess..r
    Incorrect guess: 2
    Letters already guessed: R

    Scrambled word:  NNOWRDU
    Enter your guess..o
    Incorrect guess: 3
    Letters already guessed: R

    Scrambled word:  NNOWRDU
    Enter your guess..u
    Incorrect guess: 3
    Letters already guessed: RU

    Scrambled word:  NNOWRDU
    Enter your guess..d
    Incorrect guess: 4
    Letters already guessed: RU

    Scrambled word:  NNOWRDU
    Enter your guess..o
    Incorrect guess: 5
    Letters already guessed: RU

    Scrambled word:  NNOWRDU
    Enter your guess..n
    Incorrect guess: 5
    Letters already guessed: RUN

    Scrambled word:  NNOWRDU
    Enter your guess..d
    Incorrect guess: 5
    Letters already guessed: RUND

    Scrambled word:  NNOWRDU
    Enter your guess..o
    Incorrect guess: 5
    Letters already guessed: RUNDO

    Scrambled word:  NNOWRDU
    Enter your guess..w
    Incorrect guess: 5
    Letters already guessed: RUNDOW

    Scrambled word:  NNOWRDU
    Enter your guess..n
    Incorrect guess: 5
    Letters already guessed: RUNDOWN
    Congratulations! You found the word after 5 incorrect guesses.

## Uses of if-else statement, list and loop in the program

**list[]** - It is used to store an ordered collection of items separate by commas and enclosed by brackets[].

**append()** - It adds single item to the existing list.

**join()** - It takes all the items in an iterable and join them into one string.

**shuffle()** - It randomizes the items of a list in a place. In the program it is important from the random module.

**upper()** - This functions converts all the lowercase character to the uppercase.

**print** - It is used to display the output.

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
        
A part of code inserted above shows the use of while loop and if-else statement. In the above, code while loop is used to check the condition whether the game is over or not. Under while loop. the if statement checks the letter entered by user matches with random word, and if it does not matches then it goes to else statement.








