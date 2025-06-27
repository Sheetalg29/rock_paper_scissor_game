def user():
    print("check")
def computer():
    print("check")

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