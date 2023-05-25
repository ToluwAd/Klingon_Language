"""
This program tests the users knowledge of Klingon
Author: Adejumo Toluwani
When: January 30th, 2023
"""


def main():
    """
    This function tells a user if their translation from English to Klingon is correct or wrong
    """
    user_input = input("How do you translate computer to Klingon?\n")  # Asks the user to translate to Klingon
    file = open("Klingon_English.txt", 'r')
    file.readline()    # reads the first line from klingon text
    file.readline()    # reads the second line from klingon text
    text3 = file.readline()   # reads the third line from klingon text
    index_of_line = text3.index("|")   # Gets the index of the line that separates klingon from English in the text
    klingon_language = text3[0:index_of_line]    # Stores the correct interpretation of computer in Klingon
    if user_input == klingon_language:
        print("Correct")
    else:
        print(f"Sorry, you're wrong!\nThe correct answer is {klingon_language}")


main()
