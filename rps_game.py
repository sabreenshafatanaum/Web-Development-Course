import random
options=["Rock","Paper","Scisorrs"]
user_choice=input("choose rock paper or scicorrs")
computer_choice=random.choice(options)
print("You chose:", user_choice)

print("Computer chose:", computer_choice)

if user_choice == computer_choice:

    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("Rock smashes scissors! You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("Paper covers rock! You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("Scissors cuts paper! You win!")

else:

    print("You lose!. ")