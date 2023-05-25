"""
This program asks a user to choose a Klingon consonant to practice with
Author: Adejumo Toluwani
When: January 31st, 2023
"""


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
    text = file.readlines()
    for line in text:
        if line[0] == user_choice_of_consonant or line[0:2] == user_choice_of_consonant :
            index_of_line = line.index("|")
            klingon_word = line[0:index_of_line]  # This stores the Klingon word that begins with the users consonant
            last_letter = line[-1]  # This stores the last letter of the English interpretation of the Klingon word
            english_word = line[index_of_line + 1:-1]+last_letter  # This stores the English interpretation
            english_word = english_word.replace("\n", '')  # This replaces the newline character in the text with an
            # empty string
            question = input(f"How do you translate {english_word} to Klingon? \n")
            if question == klingon_word:
                print("Correct")
            else:
                print(f"Sorry, you're wrong!\nThe correct word is {klingon_word}")


main()
