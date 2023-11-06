# Write your code here
first_name = "James"
last_name = "Bond"
full_name = first_name + " " + last_name
self_description_sentence = "My name is " +last_name+ ", " + first_name + " " + last_name + "."

cake = "vahukoor\nmarjad\ntaidis\npõhi"
print(cake)

original_string = "Programming is fun!"

# Tagurpidi sõne loomine
backwards = original_string[::-1]

# Iga teine täht
every_other = original_string[::2]

# Esimese sõna tagurpidi
first_space_index = original_string.index(" ")
first_word = original_string[:first_space_index]
first_word_reversed = first_word[::-1]

print(backwards)  # !nuf si gnimmargorP
print(every_other)  # Pormig sfn
print(first_word_reversed)  # gnimmargorP
