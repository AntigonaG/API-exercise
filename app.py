
import streamlit as st
import random

class Hangman:

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word = list(random.choice(self.possible_words))
        self.secret_word = ["_"] * len(self.word)
        self.tries = 0
        self.lives = 5
        self.wrongly_guessed_letter = []
        self.guessed_letter = []

    def display_secret_word(self):
        return " ".join(self.secret_word)

    def guess_letter(self, letter):
        if len(letter) != 1:
            return "Enter a single letter!"
        if letter in self.guessed_letter:
            return "You already entered that letter"
        else:
            self.guessed_letter.append(letter)

        if letter in self.word:
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.secret_word[i] = letter
        else:
            self.wrongly_guessed_letter.append(letter)
            self.lives -= 1

        self.tries += 1

        if self.lives == 0:
            return f"You have no more tries. The word was: {''.join(self.word)}"
        if "_" not in self.secret_word:
            return "Congratulations! You've guessed the word!"

        return ""

# Initialize game state
if 'game' not in st.session_state:
    st.session_state.game = Hangman()

game = st.session_state.game

st.title('Hangman Game')

# Display the secret word
st.write("Secret word:")
st.write(game.display_secret_word())

# Display lives left
st.write(f"Lives left: {game.lives}")

# Input for guessing a letter
letter = st.text_input("Write a letter:").lower()

# Guess button
if st.button('Guess'):
    message = game.guess_letter(letter)
    if message:
        st.write(message)

# Display wrongly guessed letters
st.write("Wrongly guessed letters:")
st.write(", ".join(game.wrongly_guessed_letter))

# Check if the game is over
if game.lives == 0 or "_" not in game.secret_word:
    if st.button('Restart Game'):
        st.session_state.game = Hangman()  # Restart the game
