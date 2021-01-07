import random


class Hangman:
    print("H A N G M A N")
    words = ['python', 'java', 'kotlin', 'javascript', 'pearl', 'ruby']
    wrong_guess = 0


    def __init__(self):
        self.option = ''
        while self.option != 'exit':
            self.start_game()

    def my_game(self):
        self.word = random.choice(self.words)
        self.hashed = list(len(self.word) * '-')
        self.gessed_letters = []
        while self.hashed != list(self.word) and self.wrong_guess < 8:
            hashed_list = ''.join(self.hashed)
            print()
            print(hashed_list)
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif guess in self.word:
                if guess in self.gessed_letters:
                    print("You already typed this letter")
                for x in range(len(self.word)):
                    if self.word[x] == guess:
                        self.hashed[x] = guess
            elif guess != guess.lower() or not guess.isalpha():
                print("It is not an ASCII lowercase letter")
            elif guess in self.gessed_letters:
                print("You already typed this letter")
            else:
                self.wrong_guess += 1
                print("No such letter in the word")
            self.gessed_letters.append(guess)
        if self.wrong_guess >= 8:
            print("You are hanged!")
            self.wrong_guess = 0
            return self.start_game()
        else:
            print(''.join(self.hashed))
            print(f"You guessed the word {self.word}!\nYou survived!")
            self.wrong_guess = 0
            return

    def start_game(self):
        self.option = input("Type 'play' to play the game, 'exit' to quit:")
        if self.option == 'play':
            return self.my_game()
        elif self.option != "exit":
            self.option = input("Type 'play' to play the game, 'exit' to quit:")
            return

Hangman()

#udt000429