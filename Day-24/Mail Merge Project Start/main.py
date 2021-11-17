#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter = ""
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
print(letter)

with open("Input/Names/invited_names.txt") as name_file:
    for name in name_file:
        output_file_name = "Output/ReadyToSend/letter_for_" + name.strip() + ".txt"
        with open(output_file_name, mode="w") as output_file:
            letter_replace = letter.replace("[name]", name.strip())
        #print(letter_replace)
            output_file.write(letter_replace)


