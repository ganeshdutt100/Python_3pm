villain = 100
player = 50

print("------Battle Started---------- ")

while villain > 0:
    print(f"Villain Health : {villain}")
    input("Press Enter to Attack 👊 ")

    villain -= player 

    if villain <= 0:
        print("Booooom! You Win!")
    else:
        print("Villain is still standing! keep hitting ")

print("---  Game Over ------")

# win +  .