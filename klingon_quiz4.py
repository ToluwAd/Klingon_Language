"""
This program asks a user to choose a Klingon consonant to practice with
Author: Adejumo Toluwani
When: February 1st, 2023
"""
import random


def main():
    """
    This function asks a user to translate an English word to a Klingon word that begins with the users input.
    """
    klingon_consonants = ["b", "ch", "D", "gh", "H", "j", "l", "m", "n", "p", "q", "Q", "r", "S", "t", "v", "w", "y",
                          "'"]
    user_choice_of_consonant = input("Which consonant do you want to practice with?\n")

    #  This block of code repeatedly asks the user for a consonant if his previous choice is not a klingon consonant.

    while user_choice_of_consonant not in klingon_consonants:
        user_choice_of_consonant = input("Which consonant do you want to practice with?\n")
    else:
        pass
    file = open("Klingon_English.txt", "r")
    text = file.readlines()  # this stores the lines of Klingon_English.txt to variable, 'text'
    for line in text:
        if line[0] == user_choice_of_consonant or line[0:2] == user_choice_of_consonant:
            index_of_line = line.index("|")
            klingon_word = line[0:index_of_line]  # This stores the Klingon word that begins with the users consonant
            last_letter = line[-1]  # This stores the last letter of the English interpretation of the Klingon word
            english_word = line[index_of_line + 1:-1]+last_letter  # This stores the English interpretation
            english_word = english_word.replace("\n", '')  # This replaces the newline character in the text with an
            # empty string
            length_of_klingon_word = len(klingon_word)
            max_attempts = 3
            attempts = 0
            continue_guessing = True
            number_of_asterisks = '*' * (length_of_klingon_word - 2)  # This is used to replace letters of the correct
            # answer in the user's first hint

            question = input(f"How do you translate {english_word} to Klingon? You have"
                             f" {max_attempts - attempts} attempts left.\n")

            # This block of code gives the user hints if he fails his first and second attempt and then returns
            # the correct answer if the user guesses wrongly on all three attempts

            while attempts < max_attempts and continue_guessing:
                attempts += 1  # This adds an attempt anytime the user guesses wrongly
                if question != klingon_word:

                    # This block of code displays the first and last letter of the correct answer

                    if attempts == 1:
                        print("Sorry, you're wrong!")
                        question = input(f"How do you translate {english_word} to Klingon? You have"
                                         f" {max_attempts - attempts} attempts left.\nHint: {klingon_word[0]}"
                                         f"{number_of_asterisks}{klingon_word[-1]}\n")

                    # This block of code displays an extra random letter from the correct answer

                    elif attempts == 2:
                        print("Sorry, you're wrong!")
                        list_of_characters = []
                        new_word = klingon_word[1:-1]  # This stores the klingon word without the extreme letters
                        random_word = random.choice(new_word)
                        for i in new_word:
                            if i != random_word:
                                list_of_characters.append(i)
                        for char in list_of_characters:
                            new_word = new_word.replace(char, '*')
                        new_word = klingon_word[0] + new_word + klingon_word[-1]
                        question = input(f"How do you translate {english_word} to Klingon? You have"
                                         f" {max_attempts - attempts} attempts left.\nHint: {new_word}\n")
                    else:
                        print(f"Sorry, you're wrong!\nThe correct answer is {klingon_word}")

                # This block of code returns correct if the user guesses correctly before his three attempts expire

                else:
                    continue_guessing = False
                    if attempts == 1:
                        print("Correct!")
                    elif attempts == 2:
                        print("Correct!")
                    else:
                        print("Correct!")


main()
