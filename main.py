import random

print("Let's play hangman!")
play_again = True
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
        guess = input("Guess a letter: ")
        if guess.isalpha() and guess.islower() and len(guess) == 1 and guess not in guessed_letters:
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

    word_display = "".join([display[i] for i in range (len(display)) if i % 2 == 0])
    if word_display == word:
      print("Word guessed, you've won!")
      break
  
  if lives == 0 or guessed == True:
      play = 0
      while play != 1 or play != 2:
          play = input("Do you want to play again(1 = yes, 2 = no)")
      if play == 2:
          print("Bye")
          break
      else:
          print("Ok, one more game")
          play_again = True
