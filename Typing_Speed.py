# To know what's your typing speed.
import time
import random

# Using 30 random jokes as sentences
SENTENCES = [
"I told my wife she was drawing her eyebrows too high. She looked surprised.",
"Parallel lines have so much in common. It’s a shame they’ll never meet.",
"I asked the librarian if the library had books on paranoia. She whispered, “They’re right behind you.”",
"Why don't skeletons fight each other? They don’t have the guts.",
"I told my computer I needed a break and now it won’t stop sending me Kit-Kat ads.",
"Why don't eggs tell jokes? They’d crack each other up.",
"I’m reading a book about anti-gravity. It’s impossible to put down.",
"Why don’t programmers like nature? It has too many bugs.",
"I wanted to be a doctor, but I didn’t have the patients.",
"My therapist says I have a preoccupation with vengeance. We’ll see about that.",
"Why don’t scientists trust atoms? Because they make up everything.",
"I used to play piano by ear, but now I use my hands.",
"Why don’t crabs give to charity? Because they’re shellfish.",
"I told my dog all my problems and he fell asleep.",
"Why don’t some couples go to therapy? Because they’d rather argue on the internet.",
"I bought a boat because it was for sail.",
"Why don’t ghosts use elevators? They lift their own spirits.",
"I’m on a whiskey diet. I’ve lost three days already.",
"Why don’t oysters donate to charity? They’re too shellfish.",
"I told my suitcase we weren’t going on vacation this year. Now I’m dealing with emotional baggage.",
"Why was the math book sad? It had too many problems.",
"I used to be addicted to the hokey pokey, but I turned myself around.",
"Why don’t cows have money? Because farmers milk them dry.",
"I’m writing a book on hurricanes. It’s only a draft so far.",
"Why don’t calendars ever get tired? They have a lot of dates.",
"I told my plants I was leaving for a week. Now they’re all rooting for me.",
"Why don’t clocks ever go out of business? They have a lot of time on their hands.",
"I tried to catch fog yesterday. Mist.",
"Why don’t mountains ever get lost? They always peak.",
"I told my fridge a joke and now it’s laughing its shelves off.",
]

def typing_test():
    print("To know your Typing Speed")
    print("-" * 50)
    print("Type the sentence exactly the same as given.")
    print("Check for the uppercase,lowercase and quotes\n")

    input("Press Enter to start...")

    sentence = random.choice(SENTENCES)
    print("\n" + sentence)
    print("-" * len(sentence)) #For Highlighting the sentence to be written.

    #Time Calculation
    start_time = time.time() #Time starts after pressing enter.
    user_input = input("\n> ")
    end_time = time.time()  #Time stops after pressing enter again.

    time_taken = end_time - start_time
    minutes = time_taken / 60

    # Calculation
    correct_characters = sum(a == b for a, b in zip(sentence, user_input)) #For comparing the user input and the sentence.
    total_characters = len(sentence)
    accuracy = (correct_characters / total_characters) * 100

    # WPM = (correct characters / 5) / minutes   
    # Assuming 5 characters are approximately equal to a word!
    words_typed = correct_characters / 5
    wpm = words_typed / minutes if minutes > 0 else 0

    # Results of your Test.
    print("\n" + "-"*50)
    print("RESULTS")
    print("-"*50)
    print(f"\nOriginal sentence: {sentence}")
    print(f"Your typed sentence: {user_input}\n")
    print("-"*50)
    print(f"Time Elapsed: {time_taken:.2f} seconds")
    print(f"Words per minute (WPM): {wpm:.1f}")
    print(f"Accuracy: {accuracy:.1f}%")
    print(f"Correct characters: {correct_characters}/{total_characters}")

    # Remarks on your Typing Speed.
    if wpm > 60:
        print("Incredible Speed! You're a typing expert!")
    elif wpm > 40:
        print("Excellent! You type very fast.")
    elif wpm > 30:
        print("Good job! You are above average wpm.")
    elif wpm > 20:
        print("Average! Keep practicing.")
    else:
        print("Keep going speed comes with practice!")

# for running the test again
if __name__ == "__main__":
    while True:
        typing_test()
        print("\n" + "-"*50)
        again = input("\nDo you want to try again? (yes/no):").lower().strip()
        if again != 'yes':
            print("Have a good day! Keep practicing!")
            break
