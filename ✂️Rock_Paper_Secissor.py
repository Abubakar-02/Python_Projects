import random

print("╔══════════════════════════════════╗")
print("║    🎮 ROCK PAPER SCISSORS 🎮     ║")
print("╚══════════════════════════════════╝")
print()

name = input("👤 Enter your Name: ")
print()
print(f"Welcome {name} ! 🐍 Lets Start the Game 🎮")
print("______________________________________________")

while True:
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    for round_num in range(1, 4):
        print()
        print(f"🎯 Round {round_num}")

        user_choice = input("What you Choose (rock/paper/scissors): ").lower()
        computer_choice = random.choice(choices)

        print(f"🤖 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("Its Draw 🤝")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🏆 You Won this Round!")
            user_score += 1
        else:
            print("💻 Computer Won this Round!")
            computer_score += 1

        print(f"⭐ Score — {name}: {user_score} | Computer: {computer_score}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print()
    print("🏆⭐🏆 Final Result")
    print(f"⭐👤 {name}: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print(f"🥇 {name} Wins! Computer Loses!")
    elif computer_score > user_score:
        print(f"💻 Computer Wins! {name} Loses!")
    else:
        print("🤝 Its a Draw Match!")

    play_again = input("\n🔄 Play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Bohat Shukriya {name}! Phir Milein gay 👋")
        break