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

while True:
    guessed = False
    if play_again == True:
        word = words.random()
        words.remove(word)
        length = len(word)
        display = ""
        for letter in word:
          display += "_ "
        display = display[0:-1]
    guess_condition == False
    while guess_condition == False:
        guess = input("Enter your guess: ")
        if guess.isalpha() and len(guess) == 1:
            guess_condition == True:
        else:
            print("Enter a proper value")
    
    right = False
    for letter in word:
        if guess == letter:
            display[word.index(letter) * 2 - 1] == letter
    
    if right = False:
        lives -= 1

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

