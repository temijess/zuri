import  random

while True:
    Rock_choice= "R"
    Scissors_choice=  "S"
    Paper_choice = "P"
    user_choice=  input("Enter your choice(R for rock, S for scissors, P for paper): ")
    possible_choices= [Rock_choice, Scissors_choice, Paper_choice]
    system_choice= random.choice(possible_choices)
    print(f"\n Player:{user_choice}, CPU:{system_choice}.\n")
    if user_choice==system_choice:
        print("it's a tie!")
    elif user_choice==Rock_choice:
        if system_choice== Paper_choice:
            print("You lose! Paper covers Rock")
        else:
            print("You win! Rock crushes Scissors")
    elif user_choice== Paper_choice:
        if system_choice==Scissors_choice:
            print("You lose! Scissors cuts Paper")
        else:
            print("You win! Paper covers Rock")
    elif user_choice==Scissors_choice:
        if system_choice==Rock_choice:
            print("You lose! Rock crushes Scissors")
        else:
            print("You win! Scissors cuts Paper")
    else:
        print("Error: Make a valid choice")
    play_again=input("Play again? Y for Yes, N for No: ")
    if play_again != "Y":
        break
