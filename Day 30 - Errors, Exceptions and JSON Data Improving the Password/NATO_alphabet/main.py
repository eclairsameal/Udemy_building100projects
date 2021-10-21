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
input_word = input("Enter a word").upper()
phonetic_code = [nato_dict[ch] for ch in list(input_word)]
print(phonetic_code)
