import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame
# for (index, row) in data.iterrows():
#     print(row.code)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    input_word = input("Enter a word").upper()
    try:
        phonetic_code = [nato_dict[ch] for ch in list(input_word)]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)

generate_phonetic()