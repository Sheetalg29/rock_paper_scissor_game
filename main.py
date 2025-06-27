print("****ROCK PAPER SCISSOR GAME***")
print("Rules of Game:\n1. Rock vs Paper -> Paper wins\n2. Rock vs Scissor -> Rock wins\n3. Paper vs Scissor -> Scissor wins")
while True:
    print("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissor\nPress 4 to Exit")
    choice = int(input("Enter your choice: "))
    while choice >3 or choice<1:
        print("Enter a valid choice:")
    if choice == 1:
        c_name = rock
    elif choice == 2:
        c_name = paper
    else:
        c_name = scissor
    print(f"Your choice is {c_name}")                
