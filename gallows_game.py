from operator import le
from random import choice

list_of_words_secrets = ["Adriana", "Ana", "Maria", "Fernando", "Leonardo", "Renatinha", "Jacob"]

word_secret: str = choice(list_of_words_secrets).lower()
letter_of_word_secret: list[str] = []

for letter in range(len(word_secret)):
    letter_of_word_secret.append("_")

opportunity: int = len(word_secret) + 4

while True:
    try:
        letter_for_word_secret: str = str(input("\nLetra para a palavra da forca: \n"))
        opportunity -= 1
    except Exception:
        print("\nOcorreu um erro. Tente novamente.")

    for letter in range(len(word_secret)):
        if(letter_for_word_secret.lower() == word_secret[letter]):
            letter_of_word_secret[letter] = letter_for_word_secret.lower() 
        
        print(letter_of_word_secret[letter], end="")

    if letter_of_word_secret == list(word_secret):
        break

    if opportunity == 0:
        print("\nInfelizmente você perdeu suas chances.")
        break