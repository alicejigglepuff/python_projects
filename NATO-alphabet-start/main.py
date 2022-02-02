student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
word_df = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_list = []
code_list = []

for (index, row) in word_df.iterrows():
    letter_list.append(row.letter)
    code_list.append(row.code)
    word_dict = {letter_list[i]:code_list[i] for i in range(len(letter_list))}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Please enter your name: ").upper()
name_letter_list = [letter for letter in name]
result = [word_dict[name_letter] for name_letter in name_letter_list]
print(result)