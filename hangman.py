import random

word_list = [
    "apple", "banana", "orange", "grape", "lemon", "mango", "peach", "melon", "berry", "cherry",
    "school", "college", "teacher", "student", "class", "homework", "exam", "pencil", "notebook", "library",
    "car", "train", "bus", "plane", "bicycle", "motor", "engine", "wheel", "brake", "travel",
    "water", "river", "ocean", "beach", "mountain", "forest", "desert", "island", "valley", "cliff",
    "happy", "sad", "angry", "scared", "brave", "smart", "funny", "kind", "honest", "loyal",
    "love", "heart", "friend", "family", "gift", "hug", "kiss", "smile", "trust", "care",
    "python", "coding", "computer", "laptop", "keyboard", "screen", "mouse", "logic", "input", "output",
    "music", "dance", "movie", "actor", "song", "guitar", "piano", "violin", "camera", "drama",
    "table", "chair", "window", "door", "lamp", "floor", "wall", "ceiling", "mirror", "clock",
    "bread", "butter", "cheese", "rice", "pizza", "pasta", "burger", "salad", "sugar", "salt"
]

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = random.choice(word_list)


dash_word = ""
for char in word :
    dash_word += "_"
print(dash_word)

game_over = False

correct_word = []

lives = 6

while game_over != True :
    guess = input("Guess a word.\n").lower()
    if guess in correct_word :
        print(f"You have already guessed {guess}")
    display = ""
    for letter in word :
        if letter == guess :
            display += guess
            correct_word.append(guess)
            print(f"You guessed {guess}, that is correct.")
        elif letter in correct_word :
            display += letter
        else :
            display += "_"
    if guess not in word :
        lives -= 1
        print(f"You guessed {guess}, that is not in the word, You lose a life.")

    print(display)
    print(hangman_pics[6 - lives])
    print(f"You have {lives} lives left.")
    if lives == 0 :
        game_over = True
        print(f"The correct word was {word}")
        print("YOU LOSE!")
    if "_" not in display :
        game_over = True
        print("CONGRATULATIONS! You won.")