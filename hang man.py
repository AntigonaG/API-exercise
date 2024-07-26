import random

class Hangman:

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word = list(random.choice(self.possible_words))
        self.secret_word = ["_"] * len(self.word)
        self.tries = 0
        self.lives = 5
        self.wrongly_guessed_letter = []
        self.error_count = 0

    def display_secret_word(self):
        print(" ".join(self.secret_word))

    def guess_letter(self):
        guessed_letter = []
        while True:
            letter = input("Write a letter:\n").lower()

            if len(letter) != 1:
                print("Enter a single letter!\n")
                continue
            if letter in guessed_letter:
                print("You already entered that letter")
                continue
            else:
                guessed_letter.append(letter)

            if letter in self.word:
                for i in range(len(self.word)):
                    if letter == self.word[i]:
                        self.secret_word[i] = letter
            else:
                self.wrongly_guessed_letter.append(letter)
                self.lives -= 1
                print(f"You have only {self.lives} lives left")

            self.tries += 1
            if self.lives == 0:
                print("You have no more tries")
                print(f"The word was: {''.join(self.word)}")
                break

            self.display_secret_word()

            if "_" not in self.secret_word:
                print("Congratulations! You've guessed the word!")
                break

# To play the game, you can create an instance of the class and call the methods.
if __name__ == "__main__":
    game = Hangman()
    while game.lives > 0 and "_" in game.secret_word:
        game.guess_letter()
