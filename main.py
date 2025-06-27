import random as r

def user():
    print("check")
def computer():
    cmp_choice = r.randint(1,3)
    print(f"{cmp_choice}")
    if cmp_choice == 1:
        cmp_name = "rock"
    elif cmp_choice == 2:
        cmp_name = "paper"
    else:
        cmp_name = "scissor"
    print(f"computer choice is {cmp_name}\n{cmp_name} vs {c_name}")
    if choice == cmp_choice:
        result = "DRAW"
    elif (choice == 1 and cmp_choice == 2) or (cmp_choice == 1 and choice == 2):
        result = 'Paper'
    elif (choice == 1 and cmp_choice == 3) or (cmp_choice == 1 and choice == 3):
        result = 'Rock'
    elif (choice == 2 and cmp_choice == 3) or (cmp_choice == 2 and choice == 3):
        result = 'Scissors'
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")          

print("****ROCK PAPER SCISSOR GAME***")
print("Rules of Game:\n1. Rock vs Paper -> Paper wins\n2. Rock vs Scissor -> Rock wins\n3. Paper vs Scissor -> Scissor wins")
while True:
    print("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissor\nPress 4 to Exit")
    choice = int(input("Enter your choice: "))
    while choice>4 or choice<1:
        choice = int(input("Enter your choice again:"))
    if choice == 1:
        c_name = "rock"
    elif choice == 2:
        c_name = "paper"
    elif choice == 4:
        break    
    else:
        c_name = "scissor"  
    print(f"Your choice is {c_name}")
    print("Opponents available:\n1. User\n2. Computer")  
    opp = int(input("Select your opponent Type:"))
    while opp>2 or opp<1:
        opp = int(input("Enter your choice again:"))
    if opp == 1:
        user()     
    else:
        computer()
        print("Do you want to play again?")
        ans = input().lower()
        if ans == n:
            break

print("Thanks for playing!")