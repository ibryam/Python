
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    input_code = str(input("Whats the word?: ")).upper()
    try:
        output = [new_dict[letter] for letter in input_code]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()