
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}

input_code = str(input("Whats the word?: ")).upper()

output = [new_dict[letter] for letter in input_code]

print(output)

