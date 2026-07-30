import time
import random

sentences = [
    "The quick brown lazy fox jumps over the lazy dog",
    "Python is a Powerful and easy to learn programming Language",
    "Practise makes a Man Perfect in every field of life",
    "Hardwork and dedication always leads to success",
    "Everyday is a new opportunity to learn something new"
]

def typing_test():
    sentence = random.choice(sentences)

    print("╔══════════════════════════════════╗")
    print("║     ⌨️  TYPING SPEED TEST  ⌨️   ║")
    print("╚══════════════════════════════════╝")
    print()
    print("📝 Type this sentence:")
    print(f"\n  {sentence}\n")
    input("Press Enter when ready......")

    start = time.time()
    user_input = input("\n✍️ Start Typing: ")
    end = time.time()

    time_taken = end - start
    words = len(sentence.split())
    wpm = (words / time_taken) * 60

    correct = sum(1 for a, b in zip(sentence, user_input) if a == b)
    accuracy = (correct / len(sentence)) * 100

    print(f"\n⏱️  Time: {time_taken:.2f} Seconds")
    print(f"🚀 WPM: {wpm:.1f}")
    print(f"🎯 Accuracy: {accuracy:.1f}%")

while True:
    typing_test()
    again = input("\n🔄 Play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 GoodBye! Keep practicing!")
        break