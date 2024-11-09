from os import write

PLACEHOLDER = "[name]"


with open("./Input/invites/names.txt") as n:
    names = n.readlines()

with open("./Input/letters/starting_letter.txt") as l:
    l_text = l.read()
    for guest in names:
        n_strip = guest.strip()
        new_l = l_text.replace(PLACEHOLDER, n_strip)

        with open(f"./Output/files_to_send/guest_{n_strip}.txt", mode = "w") as completed_file:
            completed_file.write(new_l)