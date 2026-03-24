import random
options = ["rock", "paper", "scissor"]
playing = True

while playing:
    user = input("Enter rock/paper/scissor (or 'quit' to exit): ").lower()
    if user == 'quit':
        playing = False
        continue
    if user not in options:
        print("Invalid input, try again")
        continue
    
    comp = random.choice(options)
    print(f"Computer chose: {comp}")
    
    if user == comp:
        print("Tie!")
    elif (user == "rock" and comp == "scissor") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"):
        print("You win!")
    else:
        print("Computer wins!")