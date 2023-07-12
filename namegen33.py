import os
import random

# Get the directory path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for "corpus.txt"
corpus_file_path = os.path.join(script_dir, 'corpus.txt')

with open(corpus_file_path, 'r', encoding='utf-8') as file:
    corpus = file.readlines()

first_halves = []
second_halves = []

for name in corpus:
    words = name.strip().split('|')
    if len(words) == 2:  # Check if the name has both first and second halves
        first_halves.append(words[0])
        second_halves.append(words[1])

import random

banned_end_combinations = ['tx','sl','vm','brn','kg','dm','rx','zdr','sf','aoi','km','dch','sg','aoc','fr']
banned_start_combinations = ['jp','mg','mj']
blanket_banned_combinations = ['df','rhg','nw','mjn','ebg','blr','gch','jhk','zx','uo','psk','kjr','jm','chd','bd','aou','oia','pj','aei','aue','zth','çbj','blv','aoi','aoa','aua','aui','jf','qr','dhl','rx','eou']
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'

minimum_length = 5
maximum_length = 8

def generate_name(first_halves, second_halves):
    first_part = random.choice(first_halves)
    second_part = random.choice(second_halves)

    overlap = ""

    # Check for overlap between the last character of the first part and the first character of the second part
    for i in range(len(first_part)):
        if first_part[-i:] == second_part[:i]:
            overlap = first_part[-i:]

    new_name = first_part + overlap + second_part

    # Remove consecutive repeated letters
    cleaned_name = ""
    for i in range(len(new_name)):
        if i == 0 or new_name[i] != new_name[i-1]:
            cleaned_name += new_name[i]

    # Remove repeated syllables
    split_name = cleaned_name.split("|")
    final_name = [split_name[0]]  # Initialize the final name with the first syllable
    for i in range(1, len(split_name)):
        current_syllable = split_name[i]
        previous_syllable = split_name[i - 1]
        if len(current_syllable) > 1 and current_syllable == previous_syllable:
            continue  # Skip repeating syllables
        final_name.append(current_syllable)

    final_name = "|".join(final_name)

    # Check if banned combinations are at the end, the beginning, or in blanket bans
    if final_name[-2:] in banned_end_combinations or final_name[:2] in banned_start_combinations or any(combination in final_name for combination in blanket_banned_combinations):
        return generate_name(first_halves, second_halves)  # Retry generating a new name

    # Check if the length of the final name is within the desired range
    if len(final_name) < minimum_length or len(final_name) > maximum_length:
        return generate_name(first_halves, second_halves)  # Retry generating a new name

    return final_name

num_names = 10
for _ in range(num_names):
    generated_name = generate_name(first_halves, second_halves)
    print(generated_name.encode("utf-8").decode("utf-8"))
