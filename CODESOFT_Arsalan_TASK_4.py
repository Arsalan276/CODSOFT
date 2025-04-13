# Game Rock , Paper and Scissor with Python

import random
def game(comp,user):
    if user==comp:
        return None  # Means if selected options are same then match would be tie
    elif comp=='r':
        if user=='p':
            return True
        elif user =='s':
            return False
    elif comp=='p':
        if user=='s':
            return True
        elif user =='r':
            return False
    elif comp=='s':
        if user=='p':
            return False
        elif user =='s':
            return True
while True:
    print("Computer's Turn: Rock(r), Paper(p) or Scissor(s)\n")
    #Now allowing the computer to randomly select the option without letting known to us so for this importing random library
    select_comp=random.randint(1,3)  #1-3 because we have 3 options 
    if select_comp==1:
        comp='r'
    elif select_comp==2:
        comp='p'
    elif select_comp==2:
        comp='s'
    # Now its user's turn
    user=input("Please select Rock(r), Paper(p) or Scissor(s)\n")
    result=game(comp,user)
    #To display the selected options of computer and user 
    print(f"Computer chose {comp}\n")
    print(f"You chose {user}\n")
    if result==None:
        print("Match is Tie\n")
    elif result:
        print("You Won\n")
    else:
        print("Computer Won")
    #Now asking if want to play again or not
    again=input("Do you want to play again (yes/no)").lower()
    if again!='yes':
        print("GoodBye")
        break
    

