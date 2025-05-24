import random
words=("apple","orange","banana","coconut","pineapple")

hangmanart={0:("  ",
               "   ",
               "  "),
            1:(" o ",
               "   ",
               "  "),
            2:(" o ",
               " | ",
               "   "),
            3:(" o ",
               " |\ ",
               "   "),
            4:("  o ",
               " /|\ ",
               "   "),
            5:("  o ",
               " /|\ ",
               "   \ "),
            6:("  o ",
               " /|\ ",
               " /|\ ")}
def displayman(wrongguesses):
    print("******************")
    for line in hangmanart[wrongguesses]:
        print(line)
    print("******************")    
def displayhint(hint):
    print(" ".join(hint))
def displayanswer(answer):
    print(" ".join(answer))
def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrongguesses=0 
    guessedletters=set()
    isrunning=True
    while isrunning:
        displayman(wrongguesses)
        displayhint(hint)
        guess=input("Enter a letter:").lower()
        if len(guess) !=1 or not guess.isaplha():
            print("Invalid input!")
            continue
        if guess in guessedletters:
            print(f"You have already guessed {guess}")
            continue
        guessedletters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
                    
        else:
            wrongguesses += 1      
            
        if "_" not in hint:
             displayman(wrongguesses)       
             displayanswer(answer)
             print("YOU WIN!")
             isrunning=False
        elif wrongguesses>len(hangmanart) - 1:
            displayman(wrongguesses)
            displayanswer(answer)
            print("You Loose!")
            isrunning=False
                
if __name__=='__main__':
    main()