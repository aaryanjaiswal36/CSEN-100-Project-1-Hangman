import random
lives = 6
print("Let's play hangman!")
play_again = True
words = [
    "Lantern",
    "Volcano",
    "Whisper",
    "Marble",
    "Telescope",
    "Thunder",
    "Meadow",
    "Puzzle",
    "Cinnamon",
    "Glacier",
    "Compass",
    "Velvet",
    "Dolphin",
    "Eclipse",
    "Backpack",
    "Sapphire",
    "Tornado",
    "Mushroom",
    "Keyboard",
    "Horizon",
    "Pebble",
    "Symphony",
    "Cactus",
    "Elevator",
    "Stardust",
    "Penguin",
    "Fortress",
    "Bubble",
    "Magnet",
    "Waterfall",
    "Cinnamon",
    "Orbit",
    "Feather",
    "Avalanche",
    "Pocket",
    "Rainbow",
    "Skeleton",
    "Parachute",
    "Blueprint",
    "Jellyfish",
    "Clockwork",
    "Desert",
    "Origami",
    "Lighthouse",
    "Raspberry",
    "Satellite",
    "Cobblestone",
    "Firefly",
    "Labyrinth",
    "Moonlight"
]

while play_again:
    word = random.choice(words)
    lives = 6
    guessed_letters = []
    display = ["_"] * len(word)
    guessed = False

    while guess_condition == False:
        print("Word: " + display)
        print("Lives: " + lives)
        guess = input("Enter your guess: ")
        if guess.isalpha() and len(guess) == 1 and guess in guessed_letters == False:
            guess_condition == True:
            guessed_letters.append(guess)
        else:
            print("Enter a proper value")
    
    right = False
    for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
                    right = True
    
    if right = False:
        lives -= 1

    if display == word:
        print("Word guessed, you've won!")
        guessed = True

    if lives == 0 or guessed == True:
        play = 0
        while play != 1 or play != 2:
            play = input("Do you want to play again(1 = yes, 2 = no)")
        if play = 2:
            print("Bye")
            break
        else:
            print("Ok, one more game")
            play_again = True

