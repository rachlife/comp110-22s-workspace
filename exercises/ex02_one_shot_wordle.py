"""EX02 - One-shot Wordle"""

__author__ = "730272790"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"

guess: str = input(f"What is your {len(secret)}-letter guess? ")
if len(guess) != len(secret):
    wrong_number: int = (len(guess))
    while wrong_number != len(secret):
        guess = input(f"That was not {len(secret)} letters! Try again: ")
        wrong_number = len(guess)
    # while loop to make sure the guess input is the correct number of letters
elif len(guess) == len(secret):  
    # at this point, it is confirmed that the guess input is the correct number of letters, so the part of the code which checks for correct letters begins
    i: int = 0 
    emoji: str = ""
    # starting with a blank string for emoji--the correctly colored boxes will later be concatenated 
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        # if the letter at the index of guess is also at the same index in secret, then the letter is correct and in the right place, so a green box is concatenated to the emoji string    
        else: 
            boolean: bool = False 
            alternate: int = 0
            while boolean != bool(True) and alternate < len(secret):
                # checking to see if the letter at guess index is at any of the indexes of the secret 
                if secret[alternate] == guess[i]:
                    boolean = bool(True) 
                else: 
                    alternate = alternate + 1 
             
            if boolean == bool(True):
                # if boolean is True, this means that the letter of the index of the guess does exist in the guess somewhere
                emoji += YELLOW_BOX 
            else:
                emoji += WHITE_BOX
        i = i + 1
    print(str(emoji))

    if guess != secret: 
        print("Not quite. Play again soon!")
    if len(guess) == len(secret): 
        if guess == secret: 
            print("Woo! You got it!")


    

