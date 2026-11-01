import random

print("Let's play hangman!")

words = [
    "lantern",
    "volcano",
    "whisper",
    "marble",
    "telescope",
    "thunder",
    "meadow",
    "puzzle",
    "cinnamon",
    "glacier",
    "compass",
    "velvet",
    "dolphin",
    "eclipse",
    "backpack",
    "sapphire",
    "tornado",
    "mushroom",
    "keyboard",
    "horizon",
    "pebble",
    "symphony",
    "cactus",
    "elevator",
    "stardust",
    "penguin",
    "fortress",
    "bubble",
    "magnet",
    "waterfall",
    "cinnamon",
    "orbit",
    "feather",
    "avalanche",
    "pocket",
    "rainbow",
    "skeleton",
    "parachute",
    "blueprint",
    "jellyfish",
    "clockwork",
    "desert",
    "origami",
    "lighthouse",
    "raspberry",
    "satellite",
    "cobblestone",
    "firefly",
    "labyrinth",
    "moonlight"
]

play_again = True
while play_again:
  word = random.choice(words)
  display = []
  for i in range (len(word)):
    display.append("_")
    if i != len(word) - 1:
      display.append(" ")
  lives = 6
  guessed_letters = []

  while lives > 0:
    guessed = False
    guess_condition = False
    while not guess_condition:
        print("".join(display))
        print("Lives left: " + str(lives))
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:
            guess_condition = True
            guessed_letters.append(guess)
        else:
            print("Not a valid guess. Please enter a single lowercase letter.")
    
    right = False
    for i in range(len(word)):
      if word[i] == guess:
        display[i * 2] = guess
        right = True
    
    if not right:
      lives -= 1
    if lives == 0:
      print("Out of lives, game over!")
      break

    word_display = "".join([display[i] for i in range (len(display)) if i % 2 == 0])
    if word_display == word:
      print("Word guessed, you've won!")
      break

  valid_play_again = False
  while not valid_play_again:
    play_again_question = input("Play again? (yes/no) ")
    if play_again_question == "yes":
      valid_play_again = True
      print("New game!")
    elif play_again_question == "no":
      valid_play_again = True
      play_again = False
    else:
      print("Invalid input.")
