import random

print("Let's play hangman!")
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
word = words.random()
words.remove(word)
length = len(word)
display = ""
for letter in word:
  display += "_ "
display = display[0:-1]
lives = 6
