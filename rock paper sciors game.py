import random
print("Rock Paper Scissor Game")
name = str(input("Enter your name: "))

repeat = "yes"
while repeat.lower() == "yes":  
    print("Enter your choice \n 1. Rock \n 2. paper \n 3. scissor \n")
    choice = (input("Enter your choice: "))
    
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'   
    elif choice == 3:
        choice_name = 'scissor'    
    else:
        print('''
Please, choose the options above.
Choose 1 or 2 or 3
        ''')

    print("{name}'s choice is: " + choice_name)
    comp_choice = random.randint(1,2,3)

    if comp_choice == 1:
        comp_choice_name = 'rock'    
    elif comp_choice == 2:
        comp_choice_name = 'paper'    
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)    
    print(choice_name + " VS " + comp_choice_name)

    if choice == 1 and comp_choice == 2:
        print("Computer Wins, computer picked paper.")     
    elif choice == 2 and comp_choice == 1:
        print(f"{name} Wins, {name} picked paper.")
    elif choice == 2 and comp_choice == 3:
        print("Computer Wins, computer picked scissor.")     
    elif choice == 3 and comp_choice == 2:
        print(f"{name} Wins, {name} picked scissor.")
    elif choice == 1 and comp_choice == 3:
        print(f"{name} Wins, {name} picked scissor.")
    elif choice == 3 and comp_choice == 1:
        print(f"Computer Wins, Computer picked scissor.")    
    elif choice == 3 and comp_choice == 3:
        print(f"It's a tie")
    elif choice == 1 and comp_choice == 1:
        print(f"It's a tie")
    elif choice == 2 and comp_choice == 2:
        print(f"It's a tie")
    else:
        print("Please choose option 1/2/3")

    repeat = str(input("Do you wish to play again?"))
    if repeat == "no":
        break

print("Thanks for playing")
