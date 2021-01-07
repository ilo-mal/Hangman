import random

'''print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

#hashed = ''.join('-' for c in word)

gessed_letters = []
hashed = '' #''.join([c if c in gessed_letters else "-" for c in word])

for c in word:
    if c in gessed_letters:
        hashed = ''.join(c)
    else:
        hashed = ''.join('-')

print(hashed)
wrong_guess = 0
#print(word[0] + word[1] + word[2] + (len(word) - 3) * '-')
#guess = input("Guess the word:")
for e in range(len(word) + wrong_guess):
    guess = input("Input a letter:")

    if guess in word:
        gessed_letters.append(guess)
        print(hashed)
        print(gessed_letters)

    else:
        print("No such letter in the word")
#hashed = ''.join([c if c in gessed_letters else "-" for c in word])


#if word == guess:
#    print("You survived!")
#else:
#    print("You are hanged!")'''
#print()
#print("Thanks for playing!\nWe'll see how well you did in the next stage")

    #print(hashed)
'''print("H A N G M A N\n")

word_list = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(word_list)
hashed = len(word) * '-'
hashed_list = list(hashed)


for x in range(8):
    i = 0
    print(hashed)
    guess = (input("Input a letter: > "))
    if guess not in word:
        print("No such letter in the word")
    else:
        for letters in word:
            if guess == letters:
                hashed_list[i] = guess
            i = i + 1
        hashed = "".join(hashed_list)'''
    #print()



class Hangman:
    print("H A N G M A N")
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    wrong_guess = 0
    hashed = list(len(word) * '-')
    gessed_letters = []
    def __init__(self):
        self.option = ''
        while self.option != 'exit':
            self.start_game()

    def my_game(self):
        while Hangman.hashed != list(Hangman.word) and Hangman.wrong_guess < 8:
            hashed_list = ''.join(Hangman.hashed)
            print()
            print(hashed_list)
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif guess in Hangman.word:
                if guess in Hangman.gessed_letters:
                    print("You already typed this letter")
                for x in range(len(Hangman.word)):
                    if Hangman.word[x] == guess:
                        Hangman.hashed[x] = guess
            elif guess != guess.lower() or not guess.isalpha():
                print("It is not an ASCII lowercase letter")
            elif guess in Hangman.gessed_letters:
                print("You already typed this letter")
            else:
                Hangman.wrong_guess += 1
                print("No such letter in the word")
            Hangman.gessed_letters.append(guess)
        if Hangman.wrong_guess >= 8:
            print("You are hanged!")
        else:
            print(''.join(Hangman.hashed))
            print(f"You guessed the word {Hangman.word}!\nYou survived!")

    def start_game(self):
        self.option = input("Type 'play' to play the game, 'exit' to quit:")
        if self.option == 'play':
            return Hangman.my_game(self)
        elif self.option != "exit":
            self.option = input("Type 'play' to play the game, 'exit' to quit:")
            return
Hangman()

#udt000429