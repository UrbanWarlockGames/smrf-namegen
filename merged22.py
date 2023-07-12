import os
import random
import tkinter as tk

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

banned_end_combinations = ['tx','sl','vm','brn','kg','dm','rx','zdr','sf','aoi','km','dch','sg','aoc','fr','dl']
banned_start_combinations = ['jp','mg','mj']
blanket_banned_combinations = ['df','rhg','nw','mjn','ebg','blr','gch','jhk','zx','jv','uo','psk','kjr','jm','chd','bd','aou','oia','pj','aei','aue','zth','çbj','blv','aoi','aoa','aua','aui','jf','qr','dhl','rx','eou']
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

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

import random

def generate_epithet():
    epithet = "the"
    adj_added = False
    
    if random.random() < 0.5:  # 50% chance
        adj_file = os.path.join(dir_path, "epithetsadj.txt")
        if random.random() < 0.3:  # 30% chance to add adjective
            adj = random.choice(open(adj_file).read().splitlines())
            epithet += " " + adj
            adj_added = True
        
        noun_file = os.path.join(dir_path, "epithetsnouns.txt")
        epithet += " " + random.choice(open(noun_file).read().splitlines())
    else:
        corpus_file = os.path.join(dir_path, "epithetscorpus.txt")
        epithet += " " + random.choice(open(corpus_file).read().splitlines())  # 50% chance
    
    if not adj_added and random.random() < 0.3:  # 30% chance to add "epithetsfromthe.txt"
        if random.random() < 0.7:  # 70% chance to appear on its own
            fromthe_file = os.path.join(dir_path, "epithetsfromthe.txt")
            epithet = random.choice(open(fromthe_file).read().splitlines())
        else:
            fromthe_file = os.path.join(dir_path, "epithetsfromthe.txt")
            epithet += " " + random.choice(open(fromthe_file).read().splitlines())
    
    return epithet

# Create a Tkinter window
window = tk.Tk()
window.title("Spoiled Meat, Rotten Flesh Name Generator")

# Set the window icon
icon_path = os.path.join(dir_path, "smrf.ico")
window.iconbitmap(icon_path)

# Variable to store the dark mode state
dark_mode = tk.IntVar(value=1)  # Set initial value to 1 for dark mode

# Create a Tkinter Text widget to display the generated names
text_widget = tk.Text(window, height=15, width=30)
text_widget.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)  # Grid placement with sticky option

# Create a Tkinter button to generate names
generate_button = tk.Button(window, text="Generate Names", command=generate_name, font=("Arial", 14))
generate_button.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)  # Grid placement with sticky option

# Create a Tkinter Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=0, column=2, sticky=tk.NS)  # Grid placement with sticky option

# Configure the Scrollbar to work with the Text widget
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# Function to generate names based on user input
def generate_names():
    text_widget.delete(1.0, tk.END)  # Clear the text widget
    num_results = int(result_entry.get())  # Get the user-specified number of results
    for _ in range(num_results):
        name = generate_name(first_halves, second_halves)
        epithet = generate_epithet()
        full_name = name.capitalize() + " " + epithet
        text_widget.insert(tk.END, full_name + "\n")

# Function to toggle dark mode
def toggle_dark_mode():
    if dark_mode.get() == 1:
        window.config(bg="#333333")  # Set background color
        text_widget.config(bg="#111111", fg="#ffffff")  # Set text widget colors
        generate_button.config(bg="#444444", fg="#ffffff")  # Set generate button colors
        result_label.config(bg="#333333", fg="#ffffff")  # Set label colors
        result_entry.config(bg="#555555", fg="#ffffff")  # Set entry field colors
        dark_mode_button.config(bg="#333333", fg="#ffffff", selectcolor="#333333")  # Set dark mode button colors
    else:
        window.config(bg="white")  # Set background color
        text_widget.config(bg="white", fg="black")  # Set text widget colors
        generate_button.config(bg="lightgray", fg="black")  # Set generate button colors
        result_label.config(bg="white", fg="black")  # Set label colors
        result_entry.config(bg="white", fg="black")  # Set entry field colors
        dark_mode_button.config(bg="white", fg="black", selectcolor="white")  # Set dark mode button colors

# Create a Tkinter Label and Entry for user input
result_label = tk.Label(window, text="Number of Results:")
result_label.grid(row=1, column=0, sticky=tk.E)  # Grid placement with sticky option

result_entry = tk.Entry(window)
result_entry.grid(row=1, column=1, sticky=tk.W)  # Grid placement with sticky option
result_entry.insert(tk.END, "100")  # Set the default value to 100

# Create a Tkinter button to generate names
generate_button = tk.Button(window, text="Generate Names", command=generate_names)
generate_button.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)  # Grid placement with sticky option

# Create a checkmark button for dark mode
dark_mode_button = tk.Checkbutton(window, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode)
dark_mode_button.grid(row=3, column=1, sticky=tk.SE)  # Grid placement with sticky option

# Configure row and column weights to maintain size and placement
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Call the toggle_dark_mode() function to set the GUI to dark mode initially
toggle_dark_mode()

# Set the window state to maximized
window.state('zoomed')

# Start the Tkinter event loop
window.mainloop()
