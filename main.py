import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
alphabet_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_code():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [alphabet_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_code()
    else:
        print(phonetic_code)

generate_code()
