import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

import random

def generate_name():
    name = "The"
    adj_added = False
    
    if random.random() < 0.5:  # 50% chance
        adj_file = os.path.join(dir_path, "epithetsadj.txt")
        if random.random() < 0.3:  # 30% chance to add adjective
            adj = random.choice(open(adj_file).read().splitlines())
            name += " " + adj
            adj_added = True
        
        noun_file = os.path.join(dir_path, "epithetsnouns.txt")
        name += " " + random.choice(open(noun_file).read().splitlines())
    else:
        corpus_file = os.path.join(dir_path, "epithetscorpus.txt")
        name += " " + random.choice(open(corpus_file).read().splitlines())  # 50% chance
    
    if not adj_added and random.random() < 0.3:  # 30% chance to add "epithetsfromthe.txt"
        fromthe_file = os.path.join(dir_path, "epithetsfromthe.txt")
        name += " " + random.choice(open(fromthe_file).read().splitlines())
    
    return name

for _ in range(10):
    generated_name = generate_name()
    print(generated_name)