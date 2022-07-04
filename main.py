PLACEHOLDER = "[name]"

with open("invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

with open("starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"letter_to_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
